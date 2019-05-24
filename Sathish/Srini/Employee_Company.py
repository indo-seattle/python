from flask import Flask, request

app = Flask(__name__)
print(__name__)

# Company-Employee List - Data Structure

Employee_Company = [{
    'name': 'Satish',
    'company': 'Starbucks'
},
    {
        'name': 'Dileep',
        'company': 'ATT'
    },
    {
        'name': 'Rajesh',
        'company': 'MCG'
    }

]


# GET - Get all company names
@app.route('/employee', methods=['GET'])
def get_company_list():
    emp_strings = ''
    for emp in Employee_Company:
        emp_strings += emp['company']
    print(emp_strings)
    return emp_strings


# PUT - Add employee name
@app.route('/employees', methods=['PUT','POST'])
def update_emplpyees():
    emp_data = request.get_json
    if emp_data.name in Employee_Company:
        Employee_Company.update(emp_data)
    else:
        for emp in Employee_Company:
            print(f'name is {emp.name} company is {emp.company}')
    # return


# POST


app.run(port=5000)
