#!/usr/bin/env python
'''
Create database and serves as tranport layer
'''
from flask import Flask, jsonify, request, make_response
from flask_pymongo import PyMongo
from articles import Articles
from articles_filler import Articles_filler

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'article-db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/article-db'

mongo = PyMongo(app)
articles = Articles(mongo)
filler = Articles_filler(mongo)
filler.fill_db()


@app.route('/article', methods=['GET'])
@app.route('/article/<id>')
def get_article(id=None):
    if id:
        article = articles.find_by_id(id)
        if article:
            return jsonify(article)
        return make_response(jsonify({'error': 'Not found'}), 404)
    return make_response(jsonify({'error': 'No Id entered'}), 400)


@app.route('/articles', methods=['GET'])
def get_articles():
    if request.args:
        article = articles.find_matching(request.args)
    else:
        article = articles.find_all()
    if article:
        return jsonify(article)
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, port=8888)
