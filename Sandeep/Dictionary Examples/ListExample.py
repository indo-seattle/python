
#list = [1,2,3]
#for i in range(0,len(list)):
 #   print(list[i])

name=['san','deep','Bat']
startdate=['1/1/2019','1/2/2019','1/3/2019']
enddate=['2/1/2019','2/2/2019','2/3/2019']
for row in range(0,len(name)):
    InsertQuery = "INSERT INTO OncallSchedule_Sandeep(OncallPerson,StartDate,EndDate) VALUES('"+ name[row] + "','" + startdate[row] + "','" + enddate[row] + "')"
    print(InsertQuery)

    #dict =json.loads(post_data)
    #for row in range(0,len(name)):
        #dict = {"name":name[row], "startdate":startdate[row], "enddate":enddate[row]}
        #list_of_oncalldates.append(dict)
#print(request.form.getlist('startdate'))