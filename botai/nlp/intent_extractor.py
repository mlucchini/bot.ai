from __future__ import unicode_literals

from botai.db.in_memory import InMemoryDb
from botai.model.intent import Intent


class IntentExtractor:
    def __init__(self, doc):
        self.db = InMemoryDb.instance()
        self.intents = []
        expressions = [exp for exp in self.db.expressions if exp.intent() is not None]
        if expressions:
            exp = max(expressions, key=lambda e: doc.similarity(e.model))
            self.intents = [Intent(doc.text, exp.intent().name, doc.similarity(exp.model), exp.text)]
