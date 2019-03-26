'''
tests if parser works correctly
'''
import pytest
import os
from sgm_parser import parse
from schemas import attributes, metas, fulltexts

DATA = '../data/test.sgm'


def test_parse_articles():
    with open(os.path.join(os.path.dirname(__file__), DATA), 'r') as sgml:
        articles = parse(sgml)
    assert len(articles) == 2
    for article in articles:
        assert 'date' in article
        for attribute in attributes:
            assert attribute in article
        for meta in metas:
            assert meta in article
        for fulltext in fulltexts:
            assert fulltext in article
