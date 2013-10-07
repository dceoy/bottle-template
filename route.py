from bottle import route, run, template, static_file

@route('/static/<filepath:path>')
def server_static(filepath):
  return static_file(filepath, root='static')

@route('/')
def index():
  return template('index')

run(host='localhost', port=8000, debug=True, reloader=True)
