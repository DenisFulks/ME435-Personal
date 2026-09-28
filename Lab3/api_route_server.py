import flask

app = flask.Flask(__name__)

@app.get('/')
def hello_route():
    return flask.redirect('/api/hello/Denis')

@app.route('/api/hello/<name>')
def hello_name(name):
    return f'Hello, {name}!'

app.run(host='0.0.0.0', port=8080, debug=True)