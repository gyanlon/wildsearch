from bottle import route, run, template, get, post, request
from es_add import load

@get('/update')
def update_form():
    return '''
        <form action="/update" method="post">
            <input value="Update" type="submit" />
        </form>
    '''

@post('/update') # or @route('/login', method='POST')
def do_update():
    files = load("./data/todo/")

    list = update_form()
    for file in files:
        list = list + "<div> %s - Completed </div>" % file
    return list