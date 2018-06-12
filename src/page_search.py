from bottle import route, run, template, get, post, request
from es_search import query
import json

@get('/search')
def search():
    return '''
        <form action="/search" method="post">
            <input name="querystr" type="text" />
            <input value="Search" type="submit" />
        </form>
    '''

@post('/search') # or @route('/login', method='POST')
def do_search():
    querystr = request.forms.get('querystr')
    res = query(querystr)
    s ='''
        <form action="/search" method="post">
            Username: <input name="username" type="text" />
            <input value="Search" type="submit" />
        </form>
        <div>
        %(querystr)
        </div>
    '''
    return json.dumps(res)