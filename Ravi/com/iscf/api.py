# Web APIs Exercise
#
# Copy and paste this dictionary in your code.
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

import flask
from flask import Flask
# import sys
#
# def print_states(statesnamestartswith):
#     if (statesnamestartswith):
#         statename = ""
#         for k, v in capital_dic.items():
#             if (k.startswith(statesnamestartswith)):
#
#                 statename +=  "\n " + k
#         if (statename):
#             print (statename)
#         else:
#             print (" did not match any state that starts with " + statesnamestartswith )
#
# def print_capitals(capitalnamestartswith):
#     if (capitalnamestartswith):
#         capitalname = ""
#         for k, v in capital_dic.items():
#             if (v.startswith(capitalnamestartswith)):
#                 capitalname +=  " \n" + v
#         if (capitalname):
#             print (capitalname)
#         else:
#             print ( "did not match any capital that starts with " + capitalnamestartswith )
#
# def print_capitals_given_number(numberofcapitals):
#     if (numberofcapitals != None ):
#         result =""
#         for k in list(capital_dic)[0:int(numberofcapitals)]:
#             result +=  "\n " + capital_dic[k]
#         print(result )
#
# def print_first_10():
#         result =""
#         for k in list(capital_dic)[0:10]:
#             result += "\n " + capital_dic[k]
#         print (result)
#
# def print_all():
#         result = ""
#         for k, v in capital_dic.items():
#             result += "\n " +  k  + " " + v
#         print(result)
#
# def main(arg1, arg2, arg3):
#     print_states(arg1)
#     print_capitals(arg2)
#     print_capitals_given_number(arg3)
#     print_first_10()
#     print_all()
#
#
# if __name__ == "__main__":
#     main(sys.argv[1], sys.argv[2], sys.argv[3])

app = Flask(__name__)

@app.route("/Population")
def get_population():

    state = flask.request.args.get("state")
    capital = flask.request.args.get("capital")
    statesnamestartswith = flask.request.args.get("statesnamestartswith")
    capitalnamestartswith = flask.request.args.get("capitalnamestartswith")
    numberofcapitals = flask.request.args.get("numberofcapitals")
    # firsttencapitals = flask.request.args.get("firsttencapitals")

    print(state,capital,statesnamestartswith,capitalnamestartswith,numberofcapitals, firsttencapitals)

    if (state):
        if ( capital_dic.get(state)):
            return capital_dic.get(state)
        else:
            return " did not match any state that matches " + state

    elif (capital):
        for k,v in capital_dic.items():
            if ( v == capital):
                return k
        return " did not match any capital that matches " + capital

    elif (statesnamestartswith):
        statename = ""
        for k, v in capital_dic.items():
            if (k.startswith(statesnamestartswith)):
                statename += "\n " + k
        if (statename):
            return statename
        else:
            return " did not match any state that starts with " + statesnamestartswith

    elif (capitalnamestartswith):
        capitalname = ""
        for k, v in capital_dic.items():
            if (v.startswith(capitalnamestartswith)):
                capitalname +=  "\n " + v
        if (capitalname):
            return capitalname
        else:
            return " did not match any capital that starts with " + capitalnamestartswith

    elif (numberofcapitals):
        result =""
        for k in list(capital_dic)[0:int(numberofcapitals)]:
            result += "\n " + capital_dic[k]
        return result

    else :
        result = ""
        for k, v in capital_dic.items():
            result += "\n " +  k  + " " + v
        return " Did not match any criteria + \n + printing all dictionaary " + result

@app.route("/Population/firsttencapitals")
def print_first_ten_capitals():
        result =""
        for k in list(capital_dic)[0:10]:
            result += "\n " + capital_dic[k]
        return result


app.run(port=5002, debug=True)

# Note: Write in one Pycharm file and check-in Git.
# Problem
# URL
# Create a Web API function that can return capital if we give state name.
# http://127.0.0.1:5000/Population?state=Utah
# Answer: web page displays Salt Lake City
# Create a Web API function that can return state name if we give capital name.
# http://127.0.0.1:5000/Population?capital=Richmond
# Answer: web page displays Virginia
# Create a Web API function that can return state names that starts with South
# http://127.0.0.1:5000/Population?statesnamestartswith=South
# Answer: web page displays South Carolina South Dakoda
# Create a Web API function that can return capital names that starts with Little
# http://127.0.0.1:5000/Population?capitalnamestartswith=Little
# Answer: web page displays Little Rock
# Create a Web API function that can return first 10 capital names
# http://127.0.0.1:5000/Population?firsttencapitals
# Alabama Alaska Arizona Arkansas California Colorado Connecticut Delaware Florida Georgia
#
#
#
#
#
#
# This is what we worked in the class.
# import flask
#
# app = flask.Flask(__name__)
# print(__name__)


# @app.route('/hello')
# def hello_world():
#     return "Hello Python Class, we are learning Flask a Python web framework."
#
#
# countries_population = {'India': '1.3', 'China': '1.4', 'USA': '0.32', 'Indonesia': '0.26'}
#
#
# # @app.route('/Countries') is a decorator for function: get_all_country_names();
# # The decorator helps your give a Web URL Extension,
# # in this case get_all_country_names() can be called from URL:http://127.0.0.1:5000/Countries
# @app.route('/Countries')
# def get_all_country_names():
#     result = ''
#     for _country in countries_population:
#         result += _country
#     return result
#
#
# # This is a decorator for function: get_population_by_country();
# # The decorator helps your give a Web URL Extension,
# # in this case get_population_by_country() can be called from URL:http://127.0.0.1:5000/Population
# # our function filter results by country, so you can pass that info from URL,
# # like this: http://127.0.0.1:5000/Population?country=India
# @app.route('/Population')
# def get_population_by_country():
#     # retrieve country information from URL
#     _country_name = flask.request.args.get('country')
#     # get country population information
#     return countries_population.get(_country_name)
#
#
# app.run(port=5000)

