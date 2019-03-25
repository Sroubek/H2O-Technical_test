'''
Unit tests for functions in articles.py
covering requirements of technical test
'''
import pytest
from articles import Articles
from pymongo import MongoClient
from schemas import colection

client = MongoClient('mongodb://localhost:27017')
db = client['articles-test-db']
mongo = db.articles

articles = Articles(mongo)
mongo.db.articles.drop()

mongo.db.articles.insert_many(colection)
mongo.db.articles.create_index(
    [('BODY', 'text'), ('TITLE', 'text'),
     ('DATELINE', 'text'), ('DATE', 'text')])


def test_all_articles():
    result = (articles.find_all())
    assert len(result) == 3
    assert colection.sort() == result.sort()


def test_find_matching_by_one_topic():
    result = articles.find_matching({'TOPICS': 'wheat'})
    assert len((result)) == 1
    assert 'wheat' in result[0]['TOPICS']


def test_find_matching_multyple_by_one_topic():
    assert len((articles.find_matching({'TOPICS': 'corn'}))) == 2


def test_find_matching_multyple_filters():
    assert len((articles.find_matching(
        {'TITLE': 'Test', 'COMPANIES': 'H2O'}))) == 1


def test_find_id():
    assert 1 == articles.find_by_id(1)['ID']
