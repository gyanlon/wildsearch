# -*- coding:utf-8 -*- 
from bottle import route, run, template, get, post, request, response, static_file
from es_search import query
import json
import re

@route('/images/<filename:re:.*\.gif>')
def server_static(filename):
    return static_file(filename, root="./images")

@get('/')
def search_form():
    return template('page_search')

@post('/search') # or @route('/login', method='POST')
def do_search():
    querystr = request.forms.querystr
    print("search : ", querystr)
    
    records = query(querystr)
    prettyRecords = []
    for record in records :
        record = record.replace("\r\n","").replace("\n","").replace("\r","").replace("\t","")
        print(record)
        rec = json.loads(record)
        rec = dict((k.replace("text:'","<span class=\"title\">").replace("'","</span>"), "<em>%s</em>" % v) for k, v in rec.items())
        prettyRecords.append(json.dumps(rec).encode('utf-8').decode('unicode_escape') \
            .replace("\"","") \
            .replace("{","") \
            .replace("}","") )

    return template('page_search_results', querystr=querystr, records=prettyRecords)

if __name__ == '__main__' :
    record = "{\"text:' price($)'\": \"556.0\n\"}".replace("\r\n","").replace("\n","").replace("\r","")
    json.loads(record.encode("utf-8").decode("utf-8"))