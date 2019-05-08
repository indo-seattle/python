import flask

app = flask.Flask(__name__)


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

# Create a Web API function that can return capital if we give state name.
#http://127.0.0.1:5000/Population?state=Utah
# Answer: web page displays Salt Lake City


@app.route('/returncapital')
def getcapital():
    _state_name = flask.request.args.get('state')
    return capital_dic[_state_name]


#Create a Web API function that can return state name if we give capital name.
#http://127.0.0.1:5000/Population?capital=Richmond
#Answer: web page displays Virginia


@app.route('/returnstate')
def getstatename():
    _state_capital = flask.request.args.get('capital')
    for _state_name in capital_dic:
        if capital_dic[_state_name] == _state_capital:
            return _state_name


#Create a Web API function that can return state names that starts with South
#http://127.0.0.1:5000/Population?statesnamestartswith=South
#Answer: web page displays South Carolina South Dakoda


@app.route('/Statestartswith')
def getstatestart():
    list = ''
    _start_with = flask.request.args.get('statenamestartwith')
    for _state_name in capital_dic:
        if _state_name.startswith(_start_with):
            list+=_state_name
    return list


#Create a Web API function that can return capital names that starts with Little
#http://127.0.0.1:5000/Population?capitalnamestartswith=Little
#Answer: web page displays Little Rock

@app.route('/Capitalstartwith')
def getcapitalstart():
    list = ''
    _start_with = flask.request.args.get('capitalnamestartwith')
    for _state_name in capital_dic:
        if capital_dic[_state_name].startswith(_start_with):
            list+=capital_dic[_state_name]
    return list


#Create a Web API function that can return first 10 capital names
#http://127.0.0.1:5000/Population?firsttencapitals
#Alabama Alaska Arizona Arkansas California Colorado Connecticut Delaware Florida Georgia
@app.route('/listofcapitals')
def getcapitallist():
    _list = []
    _statename = []
    for i in capital_dic:
        _statename.append(i)
    _index = 0
    _start_with = flask.request.args.get('capitalnamestartwith')
    while (_index < int(_start_with)):
        _state = _statename[_index]
        _capital = capital_dic[_state]
        list.append(_capital)
        _index += 1
    return _list


app.run(port=5000)
