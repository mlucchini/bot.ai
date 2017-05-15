from botai.nlp.english import English


def load_vocab():
    if not English.instance().nlp:
        English.instance().load()
