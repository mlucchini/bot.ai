from nose.tools import assert_greater

from botai.db.json_loader import JsonLoader


def test_json_loader():
    expressions = JsonLoader('data').expressions()
    assert_greater(len(expressions), 0)
