from datetime import datetime
from elasticsearch_dsl import DocType, Date, Integer, Keyword, Text, connections
from excel_read import read_excel
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import sys
import time

# reload(sys)
# sys.setdefaultencoding('utf-8')

# Define a default Elasticsearch client
# connections.create_connection(hosts=['localhost'])

class Article(DocType):
    title = Text(analyzer='snowball', fields={'raw': Keyword()})
    body = Text(analyzer='snowball')
    tags = Keyword()
    published_from = Date()
    lines = Integer()

    class Meta:
        index = 'doc'

    def save(self, ** kwargs):
        self.lines = len(self.body.split())
        return super(Article, self).save(** kwargs)

    def is_published(self):
        return datetime.now() > self.published_from

def update_2_es():
    # create the mappings in elasticsearch
    Article.init()

    # create and save and article
    article = Article(meta={'id': 42}, title='Hello world!', tags=['test'])
    article.body = ''' looong text '''
    article.published_from = datetime.now()
    article.save()

    article = Article.get(id=42)
    print(article.title, article.tags)
    print(article.is_published())

    # Display cluster health
    print(connections.get_connection().cluster.health())

def save2es(es, file):
    ACTIONS = []
    sheets = read_excel(file) 
    index_name = "doc"
    doc_type_name = "prd"
    count = 0
    total = 0

    # print(sheets[0]['children'][0])
    # action = {
    #     "_index": index_name,
    #     "_type": "xxx",
    #     "_source": sheets[0]['children'][0]
    # }
    # ACTIONS.append(action)             

    success, _ = bulk(es, ACTIONS, index = index_name, chunk_size=500, raise_on_error=True)    
    for sheet in sheets:
        for record in sheet['children']:
            # print (record)   

            action = {
                "_index": index_name,
                "_type": sheet['title'],
                "_source": record
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
# update_2_es()
if __name__ == '__main__':
    es = Elasticsearch(hosts=["127.0.0.1:9200"], timeout=5000)
    save2es(es, "sample.xls")