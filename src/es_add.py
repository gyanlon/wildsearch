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
import logging

def load(dir) :
    folders = []
    files = []
     
    for parent,dirnames,filenames in os.walk(dir):  
        for filename in filenames:    
            logging.info(filename)
            if(filename.endswith(".xls") or filename.endswith(".xlsx") ) :
                path = os.path.join(parent,filename)
                abspath = os.path.abspath(path)
                logging.info(abspath)
                files.append(abspath)

    logging.info("Excel files : %s" % files)

    config_analyzer_setting()
    completed_list = []
    for file in files :  
        try:      
            # abspath = os.path.abspath(file)
            save2es(file)
            completed_list.append({ "path" : file, "status" : True})
        except:
            completed_list.append({ "path" : file, "status" : False})

    logging.info("Completed files : %s" % completed_list)
    return completed_list

def save2es(file):
    logging.info("save2es : %s" % file)
    
    ACTIONS = []       
    index_name = "doc"
    doc_type_name = "prd"
    count = 0
    total = 0
    
    sheets = read_excel(file) 
    es = Elasticsearch(hosts=["{}:{}".format(constants.ES_IP, constants.ES_PORT)], timeout=5000)
    for sheet in sheets:
        for record in sheet['children']:

            action = {
                "_index": index_name,
                "_type": sheet['title'],
                "_source": {
                    "content_body": json.dumps(record).encode('utf-8').decode('unicode_escape')
                }
            }
            ACTIONS.append(action)             
            
            if( count > 0 and count % 500 == 0) :    
                logging.info (count)        
                success, _ = bulk(es, ACTIONS, index = index_name, chunk_size=500, raise_on_error=True)    
                ACTIONS = []                      
                total += success

            count = count + 1
            
        success, _ = bulk(es, ACTIONS, index = index_name, raise_on_error=True)
        total += success
    logging.info( count )

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
    logging.info(res.content)

if __name__ == '__main__' :
    # config_analyzer_setting()
    # save2es("sample.xls")
    load('./')
    # this folder is custom  
    # rootdir="./"  
    # for parent,dirnames,filenames in os.walk(rootdir):  
    #     #case 1:  
    #     for dirname in dirnames:  
    #         logging.info("parent folder is:" + parent)  
    #         logging.info("dirname is:" + dirname)  
    #     #case 2  
    #     for filename in filenames:    
    #         logging.info("parent folder is:" + parent)  
    #         logging.info("filename with full path:"+ os.path.join(parent,filename))  