from botai.db.json_loader import JsonLoader
from botai.util.singleton import Singleton


@Singleton
class InMemoryDb(object):
    def __init__(self):
        self.expressions = None
        self.loader = JsonLoader('data')

    def load(self):
        self.expressions = self.loader.expressions()
        print('Expressions loaded')
        print('   Number of expressions: %d' % len(self.expressions))
