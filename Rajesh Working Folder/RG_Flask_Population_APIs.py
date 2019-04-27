# from flask import Flask
# from flask import request
import flask

app = flask.Flask(__name__)
print(__name__)

countries_population = {'India': '1.3', 'China': '1.4', 'USA': '0.32', 'Indonesia': '0.26'}


@app.route('/countrypopulation', methods=['GET'])
def get_population():
    _country_name = flask.request.args.get('countryname')
    return countries_population.get(_country_name)


@app.route('/countries', methods=['GET'])
def get_countries():
    _country_names = ''
    for _country_name in countries_population:
        _country_names += _country_name
    return (_country_names)


app.run(port=5000)