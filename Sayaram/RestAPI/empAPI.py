from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

Employee = {"Sayaram": "Microsoft",
            "Mayukh": "Amazon",
            "Vishali": "Bright Horizon"}

@app.route('/ListData', methods = ['GET'])
def getData():
    result = ''
    data = request.args.get("Obj")
    if data == "Comp":
        for comp in Employee.values():
            result = result + comp + " "
    else:
        for emp in Employee.keys():
            result = result + emp + " "
    return result

@app.route('/Employee', methods = ['POST'])
def addData():
    if request.headers['Content-Type'] == 'application/json':
        request_data = request.get_json()
        Employee.update(request_data)
        response = Response("Added successfully", 201, mimetype='application/json')
    else:
        response = Response("Invalid state object passed in request", 400, mimetype='application/json')
    return response

@app.route('/Employee', methods = ['DELETE'])
def delData():
    emp = request.args.get("Emp")
    if emp in Employee.keys():
        Employee.pop(emp)
        response = Response("Deleted successfully", 201, mimetype='application/json')
    else:
        response = Response("Invalid state object passed in request", 400, mimetype='application/json')
    return response

@app.route('/Employee', methods = ['PUT'])
def modifyData():
    if request.headers['Content-Type'] == 'application/json':
        request_data = request.get_json()
        Employee.update(request_data)
        response = Response("Updated successfully", 201, mimetype='application/json')
    else:
        response = Response("Invalid state object passed in request", 400, mimetype='application/json')
    return response


app.run(port = 5000)