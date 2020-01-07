#!python3
from bottle import route, run, template, static_file


@route('/')
@route('/hello/<name>')
def index(name="Stranger"):
    return template('Home', name=name)


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, './static/')


run(host='0.0.0.0', port=8080, debug=True)
