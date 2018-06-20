from bottle import route, run, template, get, post, request
import page_search
import page_load 

# Note: must be 0.0.0.0
run(host='0.0.0.0', port=8080, debug=True)
