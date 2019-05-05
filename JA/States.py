# This is what we worked in the class.
from flask import Flask, request, abort

capital_dic={
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

app = Flask(__name__)
print(__name__)


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
    _country_name = request.args.get('country')
    # get country population information
    return countries_population.get(_country_name)


# This is a decorator for function: get_state_details();
# The decorator helps your give a Web URL Extension,
# in this case get_capital_of_state() can be called from URL:http://127.0.0.1:5000/State
# our function filter results by country, so you can pass that info from URL,
# like this: http://127.0.0.1:5000/State?state=Utah
@app.route('/State')
def get_state_details():

    return_msg = ""
    _not_found = True
    # check if the request is for capital
    _state = request.args.get("state")
    _capital = request.args.get('capital')
    _statesstartswith = request.args.get('statesnamestartswith')
    _capitalsstartswith = request.args.get('capitalnamestartswith')
    _firsttencapitals = request.args.get('firsttencapitals')
    # get country population information
    if _capital is not None and _capital != "":
        _state_list = capital_dic.items()
        for _each_state_tuple in _state_list:
            if _each_state_tuple[1] == _capital:
                return_msg = _each_state_tuple[0]
                _not_found = False
                break
        if _not_found:
            return_msg = "Invalid State. Please check your state"
    elif _statesstartswith is not None and _statesstartswith != "":
        _state_list = ""
        for _each_state in capital_dic:
            if _each_state.startswith(_statesstartswith):
                return_msg += _each_state
                return_msg += ' '
                _not_found = False
        if _not_found:
            return_msg = "No States Found. Please check your query"
    elif _state is not None and _state != "":
        for _each_state in capital_dic:
            if _each_state == _state:
                return_msg = capital_dic[_each_state]
                _not_found = False
        if _not_found:
            return_msg = "Invalid State. Please check your state"
    elif _capitalsstartswith is not None and _capitalsstartswith != "":
        _state_list = capital_dic.items()
        _capitals_found  = False
        for _each_state_tuple in _state_list:
            if _each_state_tuple[1].startswith(_capitalsstartswith):
                return_msg += _each_state_tuple[1]
                return_msg += ' '
                _not_found = False
        if _not_found:
            return_msg = "No Capitals Found with that string"
    elif _firsttencapitals is not None:
        _state_list = capital_dic.items()
        _count = 0
        for _each_state_tuple in _state_list:
            return_msg += _each_state_tuple[0]
            return_msg += ' '
            _count += 1
            if _count == 10:
                break
    else:
        return_msg = "Invalid Query"

    if "Invalid Query" == return_msg:
        abort(400, return_msg)
    elif _not_found is True:
        abort(404,return_msg)

    return return_msg


app.run(port=5000)

