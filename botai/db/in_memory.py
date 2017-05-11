from botai.db.json_loader import JsonLoader
from botai.util.singleton import Singleton


@Singleton
class InMemoryDb(object):
    def __init__(self):
        loader = JsonLoader('data')
        self.expressions = loader.expressions()
        print('Expressions loaded')
