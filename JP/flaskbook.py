from flask import Flask, request



app = Flask(__name__)
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
@app.route('/')
def home():
    return "<h1>Praise the Lord! Welcome to the Web API Exercise!! </h1>"


# 1. Create a Web API function that can return capital if we give state name.
# http://127.0.0.1:5000/Population?state=Utah
# Answer: web page displays Salt Lake City

def get_capital_by_state():
    _state_name = request.args.get('state')
    return "<h1> Capital of {} state  is:  <span style='color: blue'>{}</span> </h1>".format(_state_name, capital_dic.get(_state_name))
#
# 2. Create a Web API function that can return state name if we give capital name.
# http://127.0.0.1:5000/Population?capital=Richmond
# Answer: web page displays Virginia

def get_state_by_capital():
    _state_name = ''
    _capital_name = request.args.get('capital')
    for state in capital_dic:
        if capital_dic[state] == _capital_name:
            _state_name = state
    return "<h1> State name for the capital {} is : <span style='color: blue'>{}</span> </h1>".format(_capital_name,_state_name)
#
# 3. Create a Web API function that can return state names that starts with South
# http://127.0.0.1:5000/Population?statesnamestartswith=South
# Answer: web page displays South Carolina South Dakoda

def get_states_name_starts_with():
    _states_name_starts_with = request.args.get('statesnamestartswith')
    _state_name = ''
    for state in capital_dic:
        if state.startswith(_states_name_starts_with):
            _state_name += state
            _state_name += ' '
    return "<h1> State(s) that start(s) with {} is/are: <span style='color: blue'>{}</span> </h1>".format(_states_name_starts_with,_state_name)


# 4. Create a Web API function that can return capital names that starts with Little
# http://127.0.0.1:5000/Population?capitalnamestartswith=Little
# Answer: web page displays Little Rock

def get_capital_starts_with():
    _capital_name_starts_with = request.args.get('capitalnamestartswith')
    _capital_name = ''
    for state in capital_dic:
        if capital_dic[state].startswith(_capital_name_starts_with):
            _capital_name += capital_dic[state]
            _capital_name += '  '
    return "<h1> Capital(s) that start(s) with  {} is/are : <span style='color: blue'>{}</span> </h1>".format(_capital_name_starts_with, _capital_name)



# 5. Create a Web API function that can return first 10 capital names
# http://127.0.0.1:5000/Population?firsttencapitals
# Montgomery , Juneau , Phoenix , Little Rock , Sacramento , Denver , Hartford , Dover , Tallahassee , Atlanta

def get_first_ten_capitals():
    _f10cap = request.args.get('firsttencapitals')
    _capitals = ''
    _capitals_list = []
    for state, capital in capital_dic.items():
        _capitals_list.append(capital)
    for i in range(0, 10):
        _capitals += _capitals_list[i]
        _capitals += '  '
    return "<h1> First 10 Capitals in the dictionary are : <span style='color: blue'>{}</span> </h1>".format( _capitals)


@app.errorhandler(404)
def page_not_found(error):
    return "<h1><span style='color: red'> Invalid Request! </span> </h1>"




#### Main Population loop

@app.route('/Population')
def main_population():
    _state_name = request.args.get('state')
    _capital_name = request.args.get('capital')
    _states_name_starts_with = request.args.get('statesnamestartswith')
    _capital_name_starts_with = request.args.get('capitalnamestartswith')
    _f10cap = request.args.get('firsttencapitals')
    result = ""
    if _state_name is not None and _state_name!= "":
        result = get_capital_by_state()
    elif _capital_name is not None and _capital_name != "":
        result = get_state_by_capital()
    elif _states_name_starts_with is not None and _states_name_starts_with != "":
        result = get_states_name_starts_with()
    elif _capital_name_starts_with is not None and _capital_name_starts_with != "":
        result = get_capital_starts_with()
    elif _f10cap is not None:
        result = get_first_ten_capitals()
    else:
        result = page_not_found(404)
    return result



####################  Web API Excercise using the form method
##############################################################


# @app.route('/my_form_capital_by_state', methods=['POST', 'GET'])
# def my_form_capital_by_sate():
#     if request.method == 'POST':
#         state = request.form.get('state')
#         return "<h1> The capital of {} state is {} </h1>".format(state,capital_dic.get(state))
#
#     return ''' <form method="POST">
#     State <input type="text" name="state">
#     <input type="submit">
#     </form>
#     '''

# @app.route('/my_form_state_by_capital', methods=['POST', 'GET'])
# def my_form_state_by_capital():
#     if request.method == 'POST':
#         _capital_name = request.form.get('capital')
#         _state_name = " "
#         for state in capital_dic:
#             if capital_dic[state] == _capital_name:
#                 _state_name = state
#         return "<h1> {} is capital of : {} state </h1>".format(_capital_name,_state_name)
#
#     return ''' <form method="POST">
#     Capital <input type="text" name="capital">
#     <input type="submit">
#     </form>
#     '''


# @app.route('/my_form_states_name_starts_with', methods=['POST', 'GET'])
# def my_form_states_name_starts_with():
#     if request.method == 'POST':
#         _states_name_starts_with = request.form.get('statesnamestartswith')
#         _state_name = ''
#         for state in capital_dic:
#             if state.startswith(_states_name_starts_with):
#                 _state_name += state
#                 _state_name += ' '
#         return "<h1> State(s) name that start(s) with {} is/are: {} </h1>".format(_states_name_starts_with,_state_name)
#
#     return ''' <form method="POST">
#     State's name starts wih  <input type="text" name="statesnamestartswith">
#     <input type="submit">
#     </form>
#     '''



# @app.route('/my_form_capital_name_starts_with', methods=['POST', 'GET'])
# def my_form_capital_name_starts_with():
#     if request.method == 'POST':
#         _capital_name_starts_with = request.form.get('capitalnamestartswith')
#         _capital_name = ''
#         for state in capital_dic:
#             if capital_dic[state].startswith(_capital_name_starts_with):
#                 _capital_name += capital_dic[state]
#                 _capital_name += ' , '
#         return "<h1> Capitals that start(s) with {} is/are: {} </h1>".format(_capital_name_starts_with,_capital_name)
#
#     return ''' <form method="POST">
#     Capital names starts wih  <input type="text" name="capitalnamestartswith">
#     <input type="submit">
#     </form>
#     '''



# @app.route('/my_form_first_ten_capitals', methods=['POST', 'GET'])
# def my_form_first_ten_capitals():
#     if request.method == 'POST':
#         _capitals = ''
#         _capitals_list = []
#         for state, capital in capital_dic.items():
#             _capitals_list.append(capital)
#             for i in range(0, 10):
#                 _capitals += _capitals_list[i]
#                 _capitals += ' , '
#             return "<h1> First 10 Capitals in the dictionary are : {} </h1>".format( _capitals)
#
#     return ''' <form method="POST">
#     First 10 Capitals  <input type="text" name="firsttencapitals">
#     <input type="submit">
#     </form>
#     '''

#############  Exercise Web API Part -2
###########################################

countries_population = {"India": "1.3", "China": "1.4", "USA": "0.32", "Indonesia": "0.26"}

#### 1. Get all countries

# @app.route('/get_all_countries')
# def get_all_countries():
#     _country = ' '
#     for country in countries_population:
#         _country += country
#         _country += ' , '
#     return "<h1> The countries in given dictionary are : {} </h1>".format( _country)

##### 2. Add a new country using POSTMAN tool

# @app.route('/add_a_country',methods = ['POST'])
# def add_a_country():
#     requested_data = request.get_json()
#     print(requested_data)
#     countries_population.update(requested_data)
#     print(countries_population)
#     return "The new country added successfully!"

##### 3. Update country's population using POSTMAN tool

# @app.route('/update_population',methods = ['POST'])
# def update_population():
#     requested_data = request.get_json()
    # print(requested_data)
    # for state in requested_data:
    #     countries_population[state] = requested_data[state]
    # print(countries_population)
    # return "The Population(s) updated successfully!"


app.run(debug=True)
