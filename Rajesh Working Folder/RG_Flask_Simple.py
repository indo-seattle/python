import flask

app = flask.Flask(__name__)


@app.route('/hello')
def hello_world():
    return "Hello Python Class, we are learning Flask a Python web framework."


countries_population = {'India': '1.3', 'China': '1.4', 'USA': '0.32', 'Indonesia': '0.26'}


# @app.route('/Countries') is a decorator for function: get_all_country_names();
# The decorator helps your give a Web URL Extension,
# in this case get_all_country_names() can be called from URL:http://127.0.0.1:5000/Countries
@app.route('/Countries')
def get_all_country_names():
    result = ''
    for _country in countries_population:
        result += _country
    return result


# This is a decorator for function: get_population_by_country();
# The decorator helps your give a Web URL Extension,
# in this case get_population_by_country() can be called from URL:http://127.0.0.1:5000/Population
# our function filter results by country, so you can pass that info from URL,
# like this: http://127.0.0.1:5000/Population?country=India
@app.route('/Population')
def get_population_by_country():
    # retrieve country information from URL
    _country_name = flask.request.args.get('country')
    # get country population information
    return countries_population.get(_country_name)


app.run(port=5000)