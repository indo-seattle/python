from flask import Flask
from flask import request

app = Flask(__name__)
print(__name__)

countries_population = {'India': '1.3', 'China': '1.4', 'USA': '0.32', 'Indonesia': '0.26'}


# GET /population - retrieves population for a given country
@app.route('/population')
def get_population(country):
    _country_name = request.args.get('countryname')
    print(country)
    return countries_population.get(_country_name)


# GET /countries - retrieves all countries
@app.route('/countries')
def get_countries():
    _country_names = 'The countries are: '
    for _country_name in countries_population:
        _country_names += ' '
        _country_names += _country_name
    return (_country_names)


# POST /countries - Add a new country
# {'Australia': '0.4'}
@app.route('/countries', methods=['POST'])
def add_country():
    request_data = request.get_json()
    print(request_data)
    countries_population.update(request_data)
    print(countries_population)
    return 'Added successfully'


# POST /population - Update population of a country
@app.route('/population', methods=['POST'])
def update_population():
    request_data = request.get_json()
    print(request_data['India'])
    for each_item in request_data:
        countries_population[each_item] = request_data[each_item]
    print(countries_population)
    return 'Added successfully'


app.run(port=5001)

