from botai.model.expression import Expression
from botai.model.intent import Intent
from botai.nlp.english import English


def load_vocab():
    if not English.instance().nlp:
        English.instance().load()


def expression(nlp, text, intent):
    return Expression(text, nlp(text), [Intent(text, intent)])
