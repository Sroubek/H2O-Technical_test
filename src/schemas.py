
'''
module for data that are offten reused
'''
attributes = ['cgisplit', 'lewissplit', 'newid', 'topics', 'oldid']
metas = ['companies', 'exchanges', 'orgs', 'people', 'places', 'topics']
fulltexts = ['body', 'dateline', 'title']

colection = [{'_id': 1,
              'oldid': 557,
              'TITLE': 'BAHIA COCOA REVIEW',
              'TOPICS': ['corn'],
              'COMPANIES': ['H2O'],
              'DATE': '26-FEB-1987 15:03:27.51',
              'PLACES': ['el-salvador',
                         'usa',
                         'uruguay'],
              'DATELINE': 'SALVADOR, Feb 26',
              'PEOPLE': [],
              'EXCHANGES': [],
              'ORGS': [],
              'BODY': 'Such long text'},
             {'_id': 2,
              'oldid': 5571,
              'TITLE': 'BAHIA COCOA REVIEW',
              'TOPICS': ['corn',
                         'wheat'],
              'COMPANIES': ['H2O'],
              'DATE': '26-FEB-1987 15:03:27.51',
              'PLACES': ['el-salvador',
                         'usa',
                         'uruguay'],
              'DATELINE': 'SALVADOR, Feb 26',
              'PEOPLE': [],
              'EXCHANGES': [],
              'ORGS': [],
              'BODY': 'Such long text'},
             {'_id': 3,
              'oldid': 5578,
              'TITLE': 'Test 3',
              'TOPICS': ['testing'],
              'COMPANIES': ['H2O'],
              'DATE': '26-FEB-1987 15:03:27.51',
              'PLACES': ['el-salvador',
                         'usa',
                         'uruguay'],
              'DATELINE': 'SALVADOR, Feb 26',
              'PEOPLE': [],
              'EXCHANGES': [],
              'ORGS': [],
              'BODY': 'Such long text'}]


def create_article(article):
    return {
        '_id': int(
            article['newid']),
        'oldid': int(
            article['oldid']),
        'TITLE': article['title'],
        'TOPICS': article['topics'],
        'COMPANIES': article['companies'],
        'DATE': article['date'],
        'PLACES': article['places'],
        'DATELINE': article['dateline'],
        'PEOPLE': article['people'],
        'EXCHANGES': article['exchanges'],
        'ORGS': article['orgs'],
        'BODY': article['body']}
