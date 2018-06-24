from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import requests
import json
import cgi
import constants
import logging

es = Elasticsearch([{"host":constants.ES_IP,"port":constants.ES_PORT}])

def query(querystr):    
    records = query_match(querystr);

    if len(records) <= 0 :
        records = query_wildcard(querystr)

    return records

def query_match(querystr) :
    records = []
    logging.info("search:%s" % querystr)

    s = Search(using=es, index="doc") \
        .query("match", content_body=querystr) \
        .highlight("content_body", fragment_size=2048, number_of_fragments=50) \
        .highlight_options(pre_tags=["<em style='color:red;'>"], post_tags=["</em>"])

    response = s.execute()

    for hit in response:
        for fragment in hit.meta.highlight.content_body:
            records.append(fragment)

    return records

def query_wildcard(querystr) :
    records = []

    response = requests.get("http://{}:{}/_search?q={}".format(constants.ES_IP, constants.ES_PORT, querystr))
    print(response.text)
    res = json.loads(response.text)
    
    for hit in res['hits']['hits']:
        records.append(hit["_source"]["content_body"])

    return records

if __name__ == '__main__':
    print(query('丙'))
    print(u'丙')
    # print(query("中".encode('unicode_escape').decode('utf-8')))
    # print(b'\xc2\xbb'.decode('utf-8'))

    # print(len(query('13-Isopropylpodocarpa-7')))