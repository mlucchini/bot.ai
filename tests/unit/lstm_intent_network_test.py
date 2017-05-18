from __future__ import unicode_literals

from nose.tools import assert_in
from nose.tools import nottest

from botai.nlp.english import English
from test_util import expression
from test_util import load_vocab


@nottest
def test_lstm_intent_network():
    from botai.nlp.lstm_intent_network import LSTMIntentNetwork
    
    load_vocab()
    nlp = English.instance().nlp
    expressions = [
        # Needs a lot more data
        expression(nlp, 'I need a train for tomorrow', 'book_train'),
        expression(nlp, 'I will book a train', 'book_train'),
        expression(nlp, 'Please book a train for me', 'book_train'),
        expression(nlp, 'Let me book a flight for later today', 'book_flight'),
        expression(nlp, 'I need to book a flight', 'book_flight'),
        expression(nlp, 'Book at flight from Paris to London', 'book_flight'),
        expression(nlp, 'Please book me the next bus', 'book_bus'),
        expression(nlp, 'When can I book my next bus trip?', 'book_bus'),
        expression(nlp, 'I need to book a bus', 'book_bus'),
        expression(nlp, 'Get me the temperature', 'get_temperature'),
        expression(nlp, 'What is the temperature?', 'get_temperature'),
        expression(nlp, 'What is the temperature in Paris today?', 'get_temperature'),
    ]
    nn = LSTMIntentNetwork(nlp, expressions)
    nn.train()

    assert_in('book_train', intents(nn, 'I want to book a train to London'))
    assert_in('book_train', intents(nn, 'I need to book a train please'))


def intents(nn, text):
    return [intent.name for intent in nn.predict(text)]
