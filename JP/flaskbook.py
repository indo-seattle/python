import flask

app = flask.Flask(__name__)
print(__name__)

capital_dic = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
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
    'Neveda': 'Carson City',
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

#
# @app.route('/')
# def home():
#     return "<h1>Praise the Lord! Welcome to the Web API Exercise!! </h1>"


# 1. Create a Web API function that can return capital if we give state name.
# http://127.0.0.1:5000/Population?state=Utah
# Answer: web page displays Salt Lake City


# @app.route('/Population')
# def get_capital_by_state():
#     _state_name = flask.request.args.get('state')
#     return "<h1> Capital name for the given state , </h1>" +  _state_name + "<h1> is :</h1>" + capital_dic.get(_state_name)

# 2. Create a Web API function that can return state name if we give capital name.
# http://127.0.0.1:5000/Population?capital=Richmond
# Answer: web page displays Virginia


# @app.route('/Population')
# def get_state_by_capital():
#     _state_name = ''
#     _capital_name = flask.request.args.get('capital')
#     for state in capital_dic:
#         if capital_dic[state] == _capital_name:
#             _state_name = state
#     return "<h1> State name for the given capital , </h1>" +  _capital_name + "<h1> is :</h1>" + _state_name

# 3. Create a Web API function that can return state names that starts with South
# http://127.0.0.1:5000/Population?statesnamestartswith=South
# Answer: web page displays South Carolina South Dakoda


# @app.route('/Population')
# def get_states_name_starts_with():
#     _states_name_starts_with = flask.request.args.get('statesnamestartswith')
#     _state_name = ''
#     for state in capital_dic:
#         if state.startswith(_states_name_starts_with):
#             _state_name += state
#             _state_name += ' '
#     return "<h1> State(s) names that start(s) with : </h1>" +  _states_name_starts_with + "<h1> is/are :</h1>" + _state_name


# 4. Create a Web API function that can return capital names that starts with Little
# http://127.0.0.1:5000/Population?capitalnamestartswith=Little
# Answer: web page displays Little Rock


# @app.route('/Population')
# def get_capital_starts_with():
#     _capital_name_starts_with = flask.request.args.get('capitalnamestartswith')
#     _capital_name = ''
#     for state in capital_dic:
#         if capital_dic[state].startswith(_capital_name_starts_with):
#             _capital_name += capital_dic[state]
#             _capital_name += ' , '
#     return "<h1> Capital(s) that starts with : </h1>" +  _capital_name_starts_with + "<h1> is/are :</h1>" + _capital_name


# 5. Create a Web API function that can return first 10 capital names
# http://127.0.0.1:5000/Population?firsttencapitals
# Montgomery , Juneau , Phoenix , Little Rock , Sacramento , Denver , Hartford , Dover , Tallahassee , Atlanta

# @app.route('/Population')
# def get_first_ten_capitals():
#     _f10cap = flask.request.args.get('firsttencapitals')
#     _capitals = ''
#     _capitals_list = []
#     for state, capital in capital_dic.items():
#         _capitals_list.append(capital)
#     for i in range(0, 10):
#         _capitals += _capitals_list[i]
#         _capitals += ' , '
#     return "<h1> First 10 Capitals in the defined dictionary : </h1>" + _capitals


@app.errorhandler(404)
def page_not_found(error):
    return '<h1>This page does not Exist !!!</h1>', 404


app.run()
