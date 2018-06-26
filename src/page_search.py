# -*- coding:utf-8 -*- 
from bottle import route, run, template, get, post, request, response
from es_search import query
import json

@get('/')
def search_form():
    return template('page_search')

@post('/search') # or @route('/login', method='POST')
def do_search():
    querystr = request.forms.querystr
    print("search : ", querystr)
    
    records = query(querystr)
    return template('page_search_results', records=records)