from bottle import route, run, template, get, post, request
from es_search import query
import json

@get('/search')
def search_form():
    return '''
        <form action="/search" method="post">
            <input name='querystr' type="text" maxlength="255" style="height:34;width:540"/>
            <input value="查查看" type="submit" style="height:34;width:100;background:#ddd;font-size:16"/>
        </form>
    '''

@post('/search') # or @route('/login', method='POST')
def do_search():
    querystr = request.forms.get('querystr')
    records = query(querystr)
    searchform = search_form().replace("input name='querystr'", "input name='querystr' value='" + querystr + "'")
    for record in records :
      searchform = searchform + "<div style='border-bottom:medium solid #ddd;border-width: 0 0 1 0; padding-bottom: 5px'>%s</div>" % record

    return searchform