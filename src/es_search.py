from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import requests
import json
import cgi
import constants
import logging

es = Elasticsearch([{"host":constants.ES_IP,"port":constants.ES_PORT}])

def query(querystr):    
    records = []
    logging.info("search:%s" % querystr)
    # response = requests.get("http://{}:{}/_search?q=content_body:{}".format(constants.ES_IP, constants.ES_PORT, querystr))
    # res = json.loads(response.text)

    s = Search(using=es, index="doc") \
        .query("match", content_body=querystr) \
        .highlight("content_body", fragment_size=2048, number_of_fragments=50) \
        .highlight_options(pre_tags=["<em style='color:red;'>"], post_tags=["</em>"])

    response = s.execute()

    for hit in response:
        for fragment in hit.meta.highlight.content_body:
            records.append(fragment)

    # for hit in response :
    #     records.append(hit.content_body)

    return records

if __name__ == '__main__':
    print(query('13-Isopropylpodocarpa-7'))
    print(len(query('13-Isopropylpodocarpa-7')))