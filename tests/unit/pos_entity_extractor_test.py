from nose.tools import assert_equals

from botai.nlp.english import English
from botai.nlp.pos_entity_extractor import PosEntityExtractor


def test_pos_entity_extractor():
    document = English.instance().nlp(u'Steve Jobs had Apple yesterday')
    entities = PosEntityExtractor(document).entities
    assert_equals(len(entities), 3)
    assert_equals(map(lambda e: e.type, entities), ['person', 'org', 'date'])
    assert_equals(map(lambda e: e.start, entities), [0, 15, 21])
    assert_equals(map(lambda e: e.end, entities), [10, 20, 30])
