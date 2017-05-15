from __future__ import unicode_literals

import itertools
import shutil
from tempfile import mkdtemp

import spacy
from nose.tools import assert_in
from nose.tools import assert_not_in

from botai.model.expression import Expression
from botai.model.pos_entity import PosEntity
from botai.nlp.english import English
from botai.nlp.entity_trainer import EntityTrainer
from util_vocab_loader import load_vocab


def test_entity_trainer():
    output_directory = mkdtemp()
    try:
        load_vocab()
        nlp = English.instance().nlp
        trainer = EntityTrainer(nlp, output_directory)
        expressions = []
        word = 'here'
        words = [word, 'car', 'book', 'me', 'rhinoceros', 'World', 'John', 'bank', 'a']
        for L in range(0, len(words)+1):
            for subset in itertools.combinations(words, L):
                sentence = ' '.join(map(str, subset))
                if word in sentence:
                    index = sentence.index(word)
                    entities = [PosEntity(word, index, index+len(word), 'test_location')]
                    expressions.append(Expression(word, None, entities))
        trainer.train(expressions)

        nlp = spacy.load('en')
        labels_before_training = map(lambda e: e.label_, nlp(word).ents)
        assert_not_in('test_location', labels_before_training)

        nlp2 = spacy.load('en', path=output_directory)
        labels_after_training = map(lambda e: e.label_, nlp2(word).ents)
        assert_in('test_location', labels_after_training)
    finally:
        shutil.rmtree(output_directory)
