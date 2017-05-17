from botai.db.in_memory import InMemoryDb
from botai.nlp.cos_similarity_intent_extractor import CosSimilarityIntentExtractor
from botai.nlp.english import English
from botai.nlp.pos_entity_extractor import PosEntityExtractor


def get(text):
    if text:
        model = English.instance().nlp
        expressions = InMemoryDb.instance().expressions
        doc = model(text)
        pos_entities = PosEntityExtractor(doc).entities
        intents = CosSimilarityIntentExtractor(doc, expressions).intents
        entities = pos_entities + intents
        return entities
    return None
