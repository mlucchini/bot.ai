from __future__ import unicode_literals

from nose.tools import assert_equals

from botai.nlp.english import English
from botai.nlp.pos_entity_extractor import PosEntityExtractor
from test_util import load_vocab


def test_pos_entity_extractor():
    load_vocab()
    document = English.instance().nlp(u'Steve Jobs had Apple yesterday')
    entities = PosEntityExtractor(document).entities
    assert_equals(3, len(entities))
    assert_equals(['person', 'org', 'date'], map(lambda e: e.type, entities))
    assert_equals([0, 15, 21], map(lambda e: e.start, entities))
    assert_equals([10, 20, 30], map(lambda e: e.end, entities))
