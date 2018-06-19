from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import requests
import json
import cgi
import constants

es = Elasticsearch()
s = Search(using=es)

def query(querystr):    
    records = []
    print("search:", querystr)
    response = requests.get("http://{}:{}/_search?q=content_body:{}".format(constants.ES_IP, constants.ES_PORT, querystr))
    res = json.loads(response.text)

    for hit in res['hits']['hits']:
        records.append(hit["_source"])

    return records

if __name__ == '__main__':
    print(query('13-Isopropylpodocarpa-7'))
    print(len(query('13-Isopropylpodocarpa-7')))