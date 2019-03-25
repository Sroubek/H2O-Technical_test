# -*- coding: utf-8 -*-
"""
Parse data to the list and return them
"""
from bs4 import BeautifulSoup
from schemas import attributes, metas, fulltexts


def parse(file):
    articles = []
    for tag in BeautifulSoup(file, 'html.parser').find_all('reuters'):
        articles.append(tag_parser(tag))
    return articles


def tag_parser(tag):
    article = {}
    article['date'] = date_parser(tag.date)
    for attribute in attributes:
        article[attribute] = tag.get(attribute)
    for meta in metas:
        article[meta] = meta_parser(tag.find(meta))
    for fulltext in fulltexts:
        article[fulltext] = text_parser(tag.find('text'), fulltext)
    return article


def date_parser(dateTag):
    dateTag = (dateTag.string).split(' ')
    return dateTag[0]


def meta_parser(tag):
    output = []
    for d in tag.find_all('d'):
        output.append(d.string)
    return output


def text_parser(tag, innerTag):
    output = tag.find(innerTag)
    if output:
        return output.string
    return ''
