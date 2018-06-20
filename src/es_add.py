from datetime import datetime
from elasticsearch_dsl import DocType, Date, Integer, Keyword, Text, connections
from excel_read import read_excel
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import sys
import time
import requests
import json  
import os
import os.path
import constants

def load(dir) :
    folders = []
    files = []
     
    # for entry in os.scandir(dir):
    #     if entry.is_dir() :
    #         folders.append(entry.path)
    #     elif entry.is_file() and ( entry.path.endswith(".xls") or entry.path.endswith(".xlsx") ) :
    #         files.append(entry.path)
    
    for parent,dirnames,filenames in os.walk(dir):  
        for filename in filenames:    
            if(filename.endswith(".xls") or filename.endswith(".xls") ) :
                path = os.path.join(parent,filename)
                abspath = os.path.abspath(path)
                files.append(os.path.join(parent,filename))

    print("Excel files : ", files)

    config_analyzer_setting()
    completed_list = []
    for file in files :  
        try:      
            abspath = os.path.abspath(file)
            save2es(abspath)
            completed_list.append({ "path" : abspath, "status" : True})
        except:
            completed_list.append({ "path" : abspath, "status" : False})

    return completed_list

def save2es(file):

    ACTIONS = []
    sheets = read_excel(file) 
    index_name = "doc"
    doc_type_name = "prd"
    count = 0
    total = 0

    es = Elasticsearch(hosts=["127.0.0.1:9200"], timeout=5000)
    for sheet in sheets:
        for record in sheet['children']:

            action = {
                "_index": index_name,
                "_type": sheet['title'],
                "_source": {
                    "content_body": json.dumps(record)
                }
            }
            ACTIONS.append(action)             
            
            if( count > 0 and count % 500 == 0) :    
                print (count)        
                success, _ = bulk(es, ACTIONS, index = index_name, chunk_size=500, raise_on_error=True)    
                ACTIONS = []                      
                total += success

            count = count + 1
            
        success, _ = bulk(es, ACTIONS, index = index_name, raise_on_error=True)
        total += success
    print( count )

def config_analyzer_setting() :
    settings = '''
        { "settings": {
                "analysis": {
                    "char_filter": {
                        "&_to_and": {
                            "type":       "mapping",
                            "mappings": [ "&=> and "]
                    }},
                   "tokenizer": {
                        "my_tokenizer": {
                           "type": "pattern",
                           "pattern":"[^A-Za-z0-9_-]"
                    }},
                    "filter": {
                        "my_stopwords": {
                            "type":       "stop",
                            "stopwords": [ "the", "a" ]
                    }},
                    "analyzer": {
                        "my_analyzer": {
                            "type":         "custom",
                            "char_filter":  [ "html_strip", "&_to_and" ],
                            "tokenizer":    "my_tokenizer",
                            "filter":       [ "lowercase", "my_stopwords" ]
                    }}
            }},
            "mappings": {
                "_default_": {
                  "properties": {
                    "content_body": {
                      "type": "text",
                      "analyzer": "my_analyzer",
                      "search_analyzer": "my_analyzer"
                    }
                }       
            }}
        }
    '''
    res = requests.put("http://{}:{}/doc/".format(constants.ES_IP, constants.ES_PORT), settings)
    print(res.content)

if __name__ == '__main__' :
    # config_analyzer_setting()
    # save2es("sample.xls")
    load('./')
    # this folder is custom  
    # rootdir="./"  
    # for parent,dirnames,filenames in os.walk(rootdir):  
    #     #case 1:  
    #     for dirname in dirnames:  
    #         print("parent folder is:" + parent)  
    #         print("dirname is:" + dirname)  
    #     #case 2  
    #     for filename in filenames:    
    #         print("parent folder is:" + parent)  
    #         print("filename with full path:"+ os.path.join(parent,filename))  