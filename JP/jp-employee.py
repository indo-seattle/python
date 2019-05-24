from flask import Flask, request, Response



app = Flask(__name__)
print(__name__)

employees_company = {
    'Joel': 'ISCF',
    'JP': 'ATT',
    'Rajesh': 'MCG',
    'Sandesh': 'Starbucks',
    'David' : 'Amazon'}

@app.route('/employees', methods=['GET'])
def get_companies_name():
    str_company = ' '
    for employee in employees_company:
        str_company += ' ' + employees_company[employee]
    return str_company

@app.route('/add_employee', methods=['POST'])
def new_employee():
    if request.headers['Content-Type'] == 'application/json':
        request_data = request.get_json()
        print(request_data)
        employees_company.update(request_data)
        print(employees_company)
        response = Response("Added successfully", 201, mimetype='application/json')
    else:
        response = Response("Invalid employee object passed in request", 400, mimetype='application/json')
    return response



@app.route('/update_employee', methods=['PUT'])
def update_employee():
    if request.headers['Content-Type'] == 'application/json':
        request_data = request.get_json()
        print(request_data)
        employees_company.update(request_data)
        print(employees_company)
        response = Response("Added successfully", 201, mimetype='application/json')
    else:
        response = Response("Invalid state object passed in request", 400, mimetype='application/json')
    return response

@app.route('/delete_employee', methods=['DELETE'])
def delete_employee():
    request_data = request.args.get('employee')
    print(request_data)
    employees_company.pop(request_data)
    print(employees_company)
    response = Response("Deleted successfully")
    return response


app.run(debug=True)
