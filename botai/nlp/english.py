import spacy

from botai.util.singleton import Singleton


@Singleton
class English(object):
    def __init__(self):
        self.nlp = spacy.load('en', vectors='en_glove_cc_300_1m_vectors')
        print('Model loaded')
