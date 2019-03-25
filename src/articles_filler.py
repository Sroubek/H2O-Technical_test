'''
Create indexes in database and fill it with date from file
Checks if data is duplicit by comparing
 oldid and newid are same for existing object
this assume that old and new id is unique combination for every article
'''
from sgml_parser import parse
from schemas import create_article
import os


class Articles_filler:
    def __init__(self, mongo):
        self.mongo = mongo
        self.mongo.db.articles.create_index(
            [('BODY', 'text'), ('TITLE', 'text'),
             ('DATELINE', 'text'), ('DATE', 'text')])
        self.DATA = '../data/reut2-000.sgm'

    def fill_db(self):
        articles = []
        with open(os.path.join(os.path.dirname(__file__),
                               self.DATA), 'r') as sgml:
            articles = parse(sgml)
        for article in articles:
            difference = Articles_filler.check_if_same(
                article, self.mongo.db.articles)
            if difference == 'different':
                self.mongo.db.articles.replace_one(
                    {'_id': int(article['newid'])}, create_article(article))
            if not difference:
                self.mongo.db.articles.insert(create_article(article))
        print 'MongoDB succesfully inserted with data'

    @staticmethod
    def check_if_same(article, articles):
        output = articles.find_one({'_id': int(article['newid'])})
        if output:
            if (output['oldid'] == int(article['oldid'])) and (
                    output['_id'] == int(article['newid'])):
                return True
            if (output['oldid'] != int(article['oldid'])) and (
                    output['_id'] == int(article['newid'])):
                return 'different'
        return False
