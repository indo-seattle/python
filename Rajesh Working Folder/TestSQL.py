import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database = "mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers")

mycursor.execute("SELECT capital FROM states_capitals where state = 'Washington'")

#
myresult = mycursor.fetchone()
print(myresult[0])
for x in myresult:
  print(x)

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")

# sql = "INSERT INTO states_capitals (state, capital) VALUES (%s, %s)"
# val = [
#     ('Washington', 'Olympia'),
#     ('Oregon', 'Portland'),
#     ('California', 'Sacremento')
#     ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("CREATE TABLE states_capitals (state VARCHAR(255), capital VARCHAR(255))")
#
# mycursor.execute("SHOW TABLES")
#
# for x in mycursor:
#   print(x)


# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#   print(x)

# mycursor.execute("CREATE DATABASE mydatabase")


print(mydb)