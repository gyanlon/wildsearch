from bottle import route, run, template, get, post, request, response
import page_search
import page_load 
import io
import sys

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8') #改变标准输出的默认编码

# response.charset = 'utf-8'

# Note: must be 0.0.0.0
run(host='0.0.0.0', port=8080, debug=True)
# run(host='0.0.0.0', port=9080, debug=True)
