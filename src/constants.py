import os

ES_IP = "192.168.99.100"
ES_PORT = "9200"

if os.environ.get("ES_IP") != None :
    ES_IP = os.environ.get("ES_IP")
    ES_PORT = os.environ.get("ES_PORT")
