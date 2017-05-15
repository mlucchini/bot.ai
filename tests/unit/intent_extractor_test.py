from __future__ import unicode_literals

from nose.tools import assert_in

from botai.model.expression import Expression
from botai.model.intent import Intent
from botai.nlp.english import English
from botai.nlp.intent_extractor import IntentExtractor
from util_vocab_loader import load_vocab


def test_intent_extractor():
    load_vocab()
    nlp = English.instance().nlp
    expressions = [
        expression(nlp, 'I need a train for tomorrow', 'book_train'),
        expression(nlp, 'I will book a train please', 'book_train'),
        expression(nlp, 'Let me book a flight for later today please', 'book_flight'),
        expression(nlp, 'I need to book a flight', 'book_flight'),
        expression(nlp, 'Please book me the next bus', 'book_bus')
    ]
    assert_in('book_train', intents(nlp('I want to book a train to London'), expressions))
    assert_in('book_train', intents(nlp('I need to book a train please'), expressions))
    assert_in('book_flight', intents(nlp('I need to book a flight please'), expressions))
    assert_in('book_flight', intents(nlp('Book me a flight today'), expressions))


def expression(nlp, text, intent):
    return Expression(text, nlp(text), [Intent(text, intent)])


def intents(text, expressions):
    return map(lambda i: i.name, IntentExtractor(text, expressions).intents)
