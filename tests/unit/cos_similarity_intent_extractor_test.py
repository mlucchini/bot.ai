from __future__ import unicode_literals

from nose.tools import assert_in

from botai.nlp.cos_similarity_intent_extractor import CosSimilarityIntentExtractor
from botai.nlp.english import English
from test_util import load_vocab, expression


def test_intent_extractor():
    load_vocab()
    nlp = English.instance().nlp
    expressions = [
        expression(nlp, 'I need a train for tomorrow', 'book_train'),
        expression(nlp, 'I will book a train please', 'book_train'),
        expression(nlp, 'Let me book a flight for later today please', 'book_flight'),
        expression(nlp, 'I need to book a flight', 'book_flight'),
        expression(nlp, 'Please book me the next bus', 'book_bus'),
        expression(nlp, 'Set the temperature to 25 degrees', 'set_temperature'),
        expression(nlp, 'Increase the temperature by 2 degrees', 'set_temperature'),
        expression(nlp, 'What is the temperature in Paris today?', 'get_temperature'),
    ]
    assert_in('book_train', intents(nlp('I want to book a train to London'), expressions))
    assert_in('book_train', intents(nlp('I need to book a train please'), expressions))
    assert_in('book_flight', intents(nlp('I need to book a flight please'), expressions))
    assert_in('book_flight', intents(nlp('Book me a flight today'), expressions))
    assert_in('set_temperature', intents(nlp('Increase the temperature by 1 degree'), expressions))
    assert_in('set_temperature', intents(nlp('Make the temperature 20'), expressions))
    assert_in('get_temperature', intents(nlp('What is the temperature in London today?'), expressions))


def intents(text, expressions):
    return map(lambda i: i.name, CosSimilarityIntentExtractor(text, expressions).intents)
