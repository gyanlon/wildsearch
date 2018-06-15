from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import requests
import json
import cgi

es = Elasticsearch()
s = Search(using=es)

def query(querystr):    
    records = []
    print("search ： ", querystr)
    response = requests.get("http://localhost:9200/_search?q=" + querystr )
    res = json.loads(response.text)

    for hit in res['hits']['hits']:
        records.append(hit["_source"])

    return records

if __name__ == '__main__':
    print(query('13-Isopropylpodocarpa-8'))
    print(len(query('''13-Isopropylpodocarpa-8''')))
    print('-')