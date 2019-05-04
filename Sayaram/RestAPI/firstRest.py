from flask import Flask
from flask import jsonify

app = Flask(__name__)

capital_dic = {
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



@app.route("/States")
def getStates():
    return jsonify(capital_dic)

@app.route('/Population/<state>')
def get_capital_by_state(state):
    return capital_dic.get(state)

@app.route('/Population/Capital/<capital>')
def get_state_by_capital(capital):
    state = "Not_Found"
    for key, val in iter(capital_dic.items()):
        if val == capital:
            state = key
    return state


@app.route('/Population/SouthStates')
def get_south_states():
    state = []
    for key in capital_dic.keys():
        if 'South' in key:
            state.append(key)
    return ' '.join(state)

@app.route('/Population/Little/Capitals')
def get_little_states():
    capital = []
    for key, val in iter(capital_dic.items()):
        if 'Little' in val:
            capital.append(val)
    return ' '.join(capital)


app.run(port=5000)


