import flask

app = flask.Flask(__name__)

@app.route("/helloworld")
def hello_world():
    return "Hello Python Class, we are learning Flask a Python web framework."

app.run(port=5000)