from flask import Flask, request,Response
import json
app = Flask(__name__)
print(app)

months = ['January','February','March']

@app.route('/Months')
def get_all_months():
    print('I am in Get all months api')
    all_months = dict()
    for index, month in enumerate(months):
        all_months[index] = month
    return json.dumps(all_months)

@app.route('/Month', methods = ['POST'])
def add_month():
    print('Adding a month')
    status = ''
    if request.headers['Content-Type'] == 'application/json':
        req_data = request.get_json()
        print(req_data)
        #print(f"The json value {req_data['month']}")
        try:
            month = str(req_data['month']).capitalize().strip()
            print(month)
        except KeyError:
            return 'Posted data does not have month key'
        if month:
            if month not in months:
                months.append(month)
                status = 'Successfully Added'
            else:
                status = f'{month} is already in the Database'
        else:
            status = 'Empty data'

    return Response(json.dumps({"result": status}),status=200, mimetype="application/json")

@app.route('/UpdateMonth', methods = ['PUT'] )
def update_month():
    print('Updating Month....')
    update_req = request.get_json()
    status = ''
    old = ''
    new = ''
    print(update_req)
    try:
        old = update_req['old']
        new = update_req['new']
    except KeyError:
        status = 'Posted data does not have month key'
    if old == new:
        status = "Old value and new value same..not updating"
    elif old in months:
        months[months.index(old)] = new
        status = 'Successfully Updated'
    else:
        status = f'Month: {old} does not exist in the Database'

    return Response(json.dumps({"result":status}),status = 201, mimetype="application/json")

@app.route('/DeleteMonth', methods=["DELETE"])
def delete_month():
    print('Deleting month....')
    req_data = request.get_json()
    try:
        month = req_data['month']
    except KeyError:
        status = "Month key is not found"

    if month in months:
        months.remove(month)
        status = f'Month {month} deleted successfully'
    else:
        status = f'Month {month} does not exists in Database'

    return Response(json.dumps({"result": status}), status=201, mimetype="application/json")

app.run()