import flask

app = flask.Flask(__name__)

@app.route('/')
def handle_naked_domain():
    return 'Hello World!'

app.run(host='0.0.0.0', port=8080, debug=True)

if __name__ == "__main__":
    print("Running Flask")