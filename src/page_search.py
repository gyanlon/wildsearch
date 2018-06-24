# -*- coding:utf-8 -*- 
from bottle import route, run, template, get, post, request, response
from es_search import query
import json

@get('/')
def search_form():
        return '''
        <head>
        <meta http-equiv="content-type" content="text/html;charset=unicode">
        </head>
        <form action="/search" method="post">
            <input name='querystr' type="text" maxlength="255" style="height:34;width:540"/>
            <input value="查查看" type="submit" style="height:34;width:100;background:#ddd;font-size:16"/>
        </form>
    '''

@post('/search') # or @route('/login', method='POST')
def do_search():
    querystr = request.forms.querystr
    print("search : ", querystr)
    
    records = query(querystr)
    searchform = search_form().replace("input name='querystr'", "input name='querystr' value='" + querystr + "'") #show back query string
    for record in records :
      searchform = searchform + "<div style='border-bottom:medium solid #ddd;border-width: 0 0 1 0; padding-bottom: 5px'>%s</div>" % record

    return searchform