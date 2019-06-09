from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html', name = 'Raj')


@app.route('/schedule')
def schedule():
    list_of_oncalldates = [{'name': 'Sandeep', 'startdate': '1/1/2019', 'enddate': '1/14/2019'},
                           {'name': 'Srinivas', 'startdate': '1/14/2019', 'enddate': '1/28/2019'},
                           {'name': 'Riley', 'startdate': '1/28/2019', 'enddate': '2/11/2019'},
                           {'name': 'Courtney', 'startdate': '2/11/2019', 'enddate': '2/25/2019'},
                           {'name': 'Joanna', 'startdate': '2/25/2019', 'enddate': '3/4/2019'}]
    return render_template('hello.html', results=list_of_oncalldates)


@app.route('/update_on_call', methods=['POST'])
def update_on_call():
    list_of_oncalldates = request.form['each_candidate']
    list_of_oncalldates.append({'name':'Josh','startdate':'3/4/2019','enddate':'3/12/2019'})
    return render_template('hello.html', results=list_of_oncalldates)

app.run(port=5000)