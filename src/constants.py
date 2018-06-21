import os
import logging

# logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.INFO)
logging.basicConfig(level=logging.INFO,#控制台打印的日志级别
                    filename='wildsearch.log',
                    filemode='w',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )

ES_IP = "192.168.99.100"
ES_PORT = "9200"

if os.environ.get("ES_IP") != None :
    ES_IP = os.environ.get("ES_IP")
    ES_PORT = os.environ.get("ES_PORT")
