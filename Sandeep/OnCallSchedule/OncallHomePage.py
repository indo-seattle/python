from flask import Flask
from flask import render_template
from flask import request, redirect
import json

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


@app.route('/scheduledata')
def scheduledata():
    import pymysql
    import re
    try:
        con = pymysql.connect(host='ec2-34-222-119-7.us-west-2.compute.amazonaws.com', user='rajesh', password='iscfuser', db='IscfPython', use_unicode=True, charset='utf8')
        print(con)
        print('+=========================+')
        print('|  CONNECTED TO DATABASE  |')
        print('+=========================+')
    except Exception as e:
        exit('error', e)
    cur = con.cursor()
    try:
        cur.execute('SELECT OncallPerson,StartDate,EndDate FROM OncallSchedule_Sandeep')
    except Exception:
        print("Error with the query")
    data = cur.fetchall()
    print("Schedule records is - ", cur.rowcount)
    list_of_employees=[]
    for row in data:
        dict={'name':row[0],'startdate':row[1],'enddate':row[2]}
        list_of_employees.append(dict)
        print("OncallPerson= ", row[0])
        print("StartDate =", row[1])
        print("EndDate=", row[2], "\n")
    cur.close()
    return render_template('hellobkp.html' ,results =list_of_employees)


@app.route('/update_on_call', methods=['GET', 'POST'])
def update_on_call():
    import pymysql
    import re

    list_of_oncalldates=[]
    name = request.form.getlist('name')
    startdate = request.form.getlist('startdate')
    enddate = request.form.getlist('enddate')

    try:
        con = pymysql.connect(host='ec2-34-222-119-7.us-west-2.compute.amazonaws.com', user='rajesh',
                              password='iscfuser', db='IscfPython', use_unicode=True, charset='utf8')
        print(con)
        print('+=========================+')
        print('|  CONNECTED TO DATABASE  |')
        print('+=========================+')
    except Exception as e:
        exit('error', e)
    cur = con.cursor()

    try:
        cur.execute('SELECT OncallPerson,StartDate,EndDate FROM OncallSchedule_Sandeep')
    except Exception:
        print("Error with the select query")
    data = cur.fetchall()
    print("Count of records before deleting - ", cur.rowcount)

    try:
        cur.execute('DELETE FROM OncallSchedule_Sandeep')
        con.commit()
    except Exception:
        print("Error with the Delete query")

    for row in range(0, len(name)):
        InsertQuery = "INSERT INTO OncallSchedule_Sandeep(OncallPerson,StartDate,EndDate) VALUES('" + name[
            row] + "','" + startdate[row] + "','" + enddate[row] + "')"
        print(InsertQuery)
        try:
            cur.execute(InsertQuery)
            con.commit()
        except Exception:
            print("Error with the insert query")

    try:
        cur.execute('SELECT OncallPerson,StartDate,EndDate FROM OncallSchedule_Sandeep')
    except Exception:
        print("Error with the final select query")
    data = cur.fetchall()
    print("The count of records is - ", cur.rowcount)
    list_of_employees=[]
    for row in data:
        dict={'name':row[0],'startdate':row[1],'enddate':row[2]}
        list_of_employees.append(dict)
        print("OncallPerson= ", row[0])
        print("StartDate =", row[1])
        print("EndDate=", row[2], "\n")
    cur.close()
    return render_template('hellobkp.html' ,results =list_of_employees)


app.run(port=5000)