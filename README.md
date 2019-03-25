# H2O-TechnicalTest
technical test for H2O as a part of interview process

Requirements:
=============
1. API to list content 
2. API to search content
3. API get a specific content by id/any identifier

Prerequisites:
=============

1. install MongoDB
2. python 2.7
3. pipenv

Starting app:
=============

1. Clone repo
2. `$ pipenv install`
3. `$ pipenv run ./src/app.py`

Tests:
=============

1. lint: `pipenv run pycodestyle --show-source --show-pep8 ./`
2. Unit tests: `pipenv run pytest --spec --color=yes`

Endpoints:
=============

1. `/article/<id>` - return article by id, this id match newid in sgm file
2. `/articles` - without query returns all articles in database, supports following quries to fillter content:
    * `fulltext:`
        * `TITLE`
        * `BODY`
        * `DATELINE`
        * `DATE`
    * `filters:`
        * `TOPICS`
        * `COMPANIES`
        * `PLACES`
        * `PEOPLE`
        * `EXCHANGES`
        * `ORGS`
    
Examples:
=============

* `http://127.0.0.1:8888/articles?TOPICS=cocoa` - return all articles with topic `cocoa`
* `http://127.0.0.1:8888/articles?TOPICS=cocoa&TOPICS=coffee` - return all articles with topic `cocoa` and `coffee`
* `http://127.0.0.1:8888/articles?TOPICS=cocoa&TOPICS=coffee&DATE=26-FEB-1987` - return all articles with topic `cocoa` and `coffee` punlished `26-Feb-1987`
* `http://127.0.0.1:8888/articles?BODY=Bahia pressure` - find all articles with words `Bahia` and `pressure`