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
        expression(nlp, 'I will book a train please', 'book_train'),
        expression(nlp, 'Let me book a flight for later today please', 'book_flight'),
    ]
    nn = LSTMIntentNetwork(nlp, expressions)
    nn.train()

    assert_in('book_train', intents(nn, 'I want to book a train to London'))
    assert_in('book_train', intents(nn, 'I need to book a train please'))


def intents(nn, text):
    return [intent.name for intent in nn.predict(text)]
