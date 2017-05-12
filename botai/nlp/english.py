import spacy

from botai.util.singleton import Singleton

lang = 'en'


@Singleton
class English(object):
    def __init__(self):
        self.nlp = None

    def load(self, input_directory=None):
        if input_directory:
            self.nlp = spacy.load(lang, path=input_directory, add_vectors=self.__add_vectors)
        else:
            self.nlp = spacy.load(lang)
        print('Language "%s" loaded from "%s"' % (lang, input_directory))
        print('   Vocabulary size: %d' % len(self.nlp.vocab))
        print('   Vector size: %d' % self.nlp.vocab.vectors_length)

    def __add_vectors(self, vocab):
        vec_path = self.nlp.path / 'vocab' / 'vec.bin'
        if vec_path.exists():
            return vocab.load_vectors_from_bin_loc(vec_path)
