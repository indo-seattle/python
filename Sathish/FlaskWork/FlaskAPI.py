import flask
from flask import Request, Response,request
import json

app = flask.Flask(__name__)
print(__name__)

capital_dict = {
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


@app.route('/population')
def get_stats():
    print('Printing Arguments passed!')
    print(flask.request.args)
    state_name = flask.request.args.get('state')
    capital = flask.request.args.get('capital')
    state_starts = flask.request.args.get('statesnamestartswith')
    capital_starts = flask.request.args.get('capitalnamestartswith')
    first_ten = flask.request.args.get('firsttencapitals')

    print(f'Capital : {capital}')
    print(f'State : {state_name}')
    print(f'State Name Starts with : {state_starts}')
    _capital = ''

    resp_dict = {}
    if state_name is not None:
        try:
            capital_name = capital_dict[str.capitalize(state_name)]
            resp_dict.update({state_name: capital_name})
        except KeyError:
            capital_name = f'Capital not found for State: {state_name}'
            resp_dict.update({str.capitalize(state_name): capital_name})
        print(resp_dict)
        return Response(json.dumps(resp_dict), status=200, mimetype="application/json")
    elif capital is not None:
        try:
            #_capital = capital_dict[str.capitalize(capital)]
            for key, value in capital_dict.items():
                if capital_dict[key] == capital:
                    resp_dict.update({key: value})
        except KeyError:
            capital_name = f'State not found for Capital: {capital}'
            resp_dict.update({str.capitalize(state_name): capital_name})
        print(resp_dict)
        return Response(json.dumps(resp_dict), status=200, mimetype="application/json")
    elif state_starts is not None:
        try:
            for key, value in capital_dict.items():
                if key.startswith(state_starts):
                    resp_dict.update({key: value})
        except KeyError:
            capital_name = f'State not found for States starts with : {state_starts}'
            resp_dict.update({str.capitalize(state_starts): capital_name})
        print(resp_dict)
        return Response(json.dumps(resp_dict), status=200, mimetype="application/json")
    elif capital_starts is not None:
        try:
            for key, value in capital_dict.items():
                if capital_dict[key].startswith(capital_starts):
                    resp_dict.update({key: value})
        except KeyError:
            capital_name = f'State not found for States starts with : {state_starts}'
            resp_dict.update({str.capitalize(capital_starts): capital_name})
        print(resp_dict)
        return Response(json.dumps(resp_dict), status=200, mimetype="application/json")
    elif first_ten is not None:
        counter = 0
        try:
            for key, value in capital_dict.items():
                counter += 1
                resp_dict.update({key: value})
                if counter == 10:
                    break
        except KeyError:
            capital_name = f'State not found for States starts with : {state_starts}'
            resp_dict.update({str.capitalize(capital_starts): capital_name})
        print(resp_dict)
        return Response(json.dumps(resp_dict), status=200, mimetype="application/json")


@app.teardown_request
def show_teardown(exception):
    print('after with block')

@app.route('/')
def index():
    return '/population  to get popultion info'

app.run()