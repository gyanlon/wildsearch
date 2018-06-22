from bottle import route, run, template, get, post, request
from es_add import load

@get('/load')
def update_form():
    return '''
        <form action="/load" method="post">
            <input value="Load" type="submit" />
        </form>
    '''

@post('/load') # or @route('/login', method='POST')
def do_update():
    results = load("/data/todo/")

    list = update_form()
    for result in results:
        list = list + "<div> {} - {} </div>".format(result["path"], "Completed" if result["status"] else "Error")
    return list

if __name__ == '__main__' :
    res = do_update()    
    print(res)