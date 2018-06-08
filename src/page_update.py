from bottle import route, run, template, get, post, request
from es_add import update_2_es

@get('/update')
def update():
    return '''
        <form action="/update" method="post">
            <input value="Update" type="submit" />
        </form>
    '''

@post('/update') # or @route('/login', method='POST')
def do_update():
    update_2_es()