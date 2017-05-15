from __future__ import unicode_literals

from botai.model.intent import Intent


class IntentExtractor:
    def __init__(self, doc, expressions):
        self.intents = []
        expressions_with_intent = [exp for exp in expressions if exp.intent() is not None]
        if expressions_with_intent:
            exp = max(expressions_with_intent, key=lambda e: doc.similarity(e.doc))
            self.intents = [Intent(doc.text, exp.intent().name, doc.similarity(exp.doc), exp.text)]
