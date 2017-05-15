from botai.db.in_memory import InMemoryDb
from botai.nlp.english import English
from botai.nlp.intent_extractor import IntentExtractor
from botai.nlp.pos_entity_extractor import PosEntityExtractor


def get(text):
    if text:
        model = English.instance().nlp
        expressions = InMemoryDb.instance().expressions
        doc = model(text)
        pos_entities = PosEntityExtractor(doc).entities
        intents = IntentExtractor(doc, expressions).intents
        entities = pos_entities + intents
        return entities
    return None
