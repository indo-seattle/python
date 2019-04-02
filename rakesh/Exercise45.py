print("Exercise 45 - Python Set")
print("Python items superset function.")

myset1 = {"NFL", "Cricket", "Baseball"}
myset2 = {"NFL", "Cricket"}

print(myset1.issuperset(myset2))
print(myset2.issuperset(myset1))