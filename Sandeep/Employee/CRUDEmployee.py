from flask import Flask
from flask import request
from flask import Response

appAPI=Flask(__name__)
print(__name__)

employee = {'Sandeep':'MCG'}


print ( employee.get('Sandeep'))


@appAPI.route('/employee',methods =['GET'])
def get_employee():
    return employee.get('Sandeep')


@appAPI.route('/employeeupdate', methods=['PUT'])
def update_employee():
    company_name = request.args.get("Sandeep")
    #employee_name = request.args.getlist[0]
    #company_name = request.args.get(employee_name)
    employee.update(Sandeep=company_name)
    return employee.get('Sandeep')


@appAPI.route('/employeecreate', methods=['POST'])
def create_employee():
    if request.headers['Content-Type'] == 'application/json':
        request_data = request.get_json()
        print(request_data)
        employee.update(request_data)
        print(employee)
        response = Response("Added successfully", 201, mimetype='application/json')
    else:
        response = Response("Invalid state object passed in request", 400, mimetype='application/json')
    return response
#
# @appAPI.route('/employeecreate', methods=['POST'])
# def create_employee():
#     request_data = request.get_json()
#     print(request_data)
#     employee.update(request_data)
#     print(employee)


appAPI.run(port=5005)

