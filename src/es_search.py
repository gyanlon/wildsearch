from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

client = Elasticsearch()

s = Search(using=client)
#s = Search(using=client, index="my-index") \
#    .filter("term", category="search") \
#    .query("match", title="python")   \
#    .exclude("match", description="beta")

def query(querystr):
    querystring = "*" + querystr + "*"
    print(querystring)
    res = client.search(index="", body={"query":{"wildcard":{"body":"*"}}})

    return res

# print(query('love'))