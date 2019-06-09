import mysql.connector

from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)
print(__name__)

capitals_data={
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

#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="1234",
#   database = "mydatabase"
# )


mydb = mysql.connector.connect(
  host="ec2-34-222-119-7.us-west-2.compute.amazonaws.com",
  user="rajesh",
  passwd="iscfuser",
  database = "IscfPython"
)

# # GET /population - returns all capitals in one string
# @app.route('/capitals', methods=['GET'])
# def get_capitals():
#     str_capitals = ''
#     for each_state in capitals_data:
#         str_capitals += ' ' + capitals_data[each_state]
#     return str_capitals


# GET /population - returns all capitals in one string
@app.route('/capitals', methods=['GET'])
def get_capitals():
    str_capitals = ''
    mycursor = mydb.cursor()
    mycursor.execute("SELECT capital FROM states_capitals")
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)
        str_capitals += ' ' + row[0]
    return str_capitals


# GET /capital - returns capital for a state
@app.route('/capital', methods=['GET'])
def get_capital_for_state():
    state_name = request.args.get('state')
    if state_name:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT capital FROM states_capitals where state = '" + state_name + "'")
        myresult = mycursor.fetchone()
        if myresult:
            return myresult[0]
        else:
            return Response("There is no content to send for this request", 204, mimetype='application/json')
            #return "There is no content to send for this request."
    else:
        return "Received empty string. Send valid state name."


# POST /state - Add a new state
# {'Telangana': 'Hyderabad'}
# @app.route('/state', methods=['POST'])
# def add_state():
#     if request.headers['Content-Type'] == 'application/json':
#         request_data = request.get_json()
#         print(request_data)
#         capitals_data.update(request_data)
#         print(capitals_data)
#         response = Response("Added successfully", 201, mimetype='application/json')
#     else:
#         response = Response("Invalid state object passed in request", 400, mimetype='application/json')
#     return response


@app.route('/state', methods=['POST'])
def add_state():
    if request.headers['Content-Type'] == 'application/json':
        request_data = request.get_json()
        print(request_data)
        sql = "INSERT INTO states_capitals (state, capital) VALUES (%s, %s)"
        val = tuple(request_data.items())
        # val = ("John", "Highway 21")
        print(val)
        mycursor = mydb.cursor()
        mycursor.executemany(sql, val)
        mydb.commit()
        response = Response("Added successfully", 201, mimetype='application/json')
    else:
        response = Response("Invalid state object passed in request", 400, mimetype='application/json')
    return response

# # PUT /state - Add a new state
# # {'Telangana': 'Hyderabad1'}
# @app.route('/state', methods=['PUT'])
# def update_state():
#     if request.headers['Content-Type'] == 'application/json':
#         request_data = request.get_json()
#         print(request_data)
#         capitals_data.update(request_data)
#         print(capitals_data)
#         response = Response("Added successfully", 201, mimetype='application/json')
#     else:
#         response = Response("Invalid state object passed in request", 400, mimetype='application/json')
#     return response


app.run(port=5002)