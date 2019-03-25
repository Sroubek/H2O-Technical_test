'''
Article query service taking data from articles-db
'''
from bson import ObjectId


class Articles:
    def __init__(self, mongo):
        self.mongo = mongo

    def find_all(self):
        articles = self.mongo.db.articles
        output = []
        print 'find all'
        for q in articles.find():
            output.append(Articles.make_object(q))
        return output

    def find_matching(self, query={}):
        articles = self.mongo.db.articles
        output = []
        for q in articles.find(Articles.create_input(query)):
            output.append(Articles.make_object(q))
        return output

    def find_by_id(self, query={}):
        articles = self.mongo.db.articles
        output = articles.find_one({'_id': int(query)})
        return Articles.make_object(output)

    @staticmethod
    def make_object(q):
        print q['oldid']
        return {
            'ID': q['_id'],
            'oldid': q['oldid'],
            'TITLE': q['TITLE'],
            'TOPICS': q['TOPICS'],
            'COMPANIES': q['COMPANIES'],
            'DATE': q['DATE'],
            'PLACES': q['PLACES'],
            'DATELINE': q['DATELINE'],
            'PEOPLE': q['PEOPLE'],
            'EXCHANGES': q['EXCHANGES'],
            'ORGS': q['ORGS'],
            'BODY': q['BODY']}

    @staticmethod
    def create_input(query):
        input = {}
        for x in query:
            if x == 'BODY' or x == 'TITLE':
                input['$text'] = {'$search': query[x]}
            else:
                input[x] = query[x]
        return input
