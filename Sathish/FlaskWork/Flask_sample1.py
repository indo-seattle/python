import flask
app = flask.Flask(__name__)
print(__name__)
countries_population = {'India':'1.3', 'China': '1.4', 'USA': '0.32', 'Indonesia': '0.26'}

@app.route('/hello')
def helloWorld():
    return "Hellow Python Class, This is my first return"

app.run(port=5000)

