from __future__ import unicode_literals

import shutil
from tempfile import mkdtemp

import spacy
from nose.tools import assert_in
from nose.tools import assert_not_in

from botai.model.expression import Expression
from botai.model.pos_entity import PosEntity
from botai.nlp.entity_trainer import EntityTrainer


def test_entity_trainer():
    output_directory = mkdtemp()
    try:
        trainer = EntityTrainer(output_directory)
        expressions = [
            Expression('here', [PosEntity('here', 0, 4, 'test_location')]),
            Expression('Here', [PosEntity('Here', 0, 4, 'test_location')]),
            Expression('A here', [PosEntity('here', 2, 6, 'test_location')]),
            Expression('B here', [PosEntity('here', 2, 6, 'test_location')]),
            Expression('Here too', [PosEntity('Here', 0, 4, 'test_location')]),
            Expression('Here me', [PosEntity('Here', 0, 4, 'test_location')]),
            Expression('Here in', [PosEntity('Here', 0, 4, 'test_location')])]
        trainer.train(expressions)

        text = 'Here'
        nlp = spacy.load('en')
        nlp2 = spacy.load('en', path=output_directory)

        labels_before_training = map(lambda e: e.label_, nlp(text).ents)
        assert_not_in(labels_before_training, ['test_location'])

        labels_after_training = map(lambda e: e.label_, nlp2(text).ents)
        assert_in(labels_after_training, ['test_location'])
    finally:
        shutil.rmtree(output_directory)
