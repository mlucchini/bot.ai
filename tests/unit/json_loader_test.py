from __future__ import unicode_literals

from nose.tools import assert_less

from botai.db.json_loader import JsonLoader


def test_json_loader():
    expressions = JsonLoader('data').expressions()
    assert_less(0, len(expressions))
