# EXERCISES RELATED TO LISTS

list_of_week_days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

#Print 3rd item in the list
#Method 1
for i in list_of_week_days:
    if list_of_week_days.index(i) == 2:
        print("Third element in list is", i)
#Method 2
print("Third element in list is", list_of_week_days[2])


#Print length of list
#Method 1
count = 0
for i in list_of_week_days:
    count += 1
print("Length of the list is:", count)
#Method 2
print("Length of the list is:", len(list_of_week_days))

#Remove Friday from the list.
for i in list_of_week_days:
    if i == 'Friday':
        j=list_of_week_days.index(i)
        list_of_week_days.pop(j)
print(list_of_week_days)

#Add Friday to the list before Saturday
#for i in list_of_week_days:
#   if i == 'Saturday':
#       j = list_of_week_days.index(i)
#      list_of_week_days.insert(j, 'Friday')
#print(list_of_week_days)

#Add another Monday value to the list
list_of_week_days.append('Monday')
print(list_of_week_days)

#Print number of times Monday occured in the list.
count = 0
for i in list_of_week_days:
    if i == 'Monday':
        count += 1
print("Number of times Monday appeared:", count)

#Remove Monday from the list
for i in list_of_week_days:
    if i == 'Monday':
        j = list_of_week_days.index(i)
        list_of_week_days.pop(j)
print(list_of_week_days)

#Print the list by reversing it
list_of_week_days.reverse()
print(list_of_week_days)

#Print the list by sorting ascending and descending
list_of_week_days.sort(reverse=False)
print(list_of_week_days)
list_of_week_days.sort(reverse=True)
print(list_of_week_days)

#Print all the items in the list using for loop
for i in list_of_week_days:
    print(i)

#Print all the index values for each item in the list (loop)
for i in list_of_week_days:
    print(i, "--", list_of_week_days.index(i))

#Print all the items from last to first in the list (loop)
l = len(list_of_week_days)
while (l>0):
    print(list_of_week_days[l-1])
    l=l-1

#Print all odd items in the list
print("All odd items in the list")
for i in list_of_week_days:
    j = list_of_week_days.index(i)
    if (j%2 == 0):
        print(list_of_week_days[j])

#Print all the even items in the list
print("All even items in the list")
for i in list_of_week_days:
    j = list_of_week_days.index(i)
    if (j % 2 == 0):
        print(list_of_week_days[j])

#Print “Thursday is the fifth day of the week” going through the loop and if list has Thursday
list_of_week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for i in list_of_week_days:
    if i == 'Thursday':
        print(i,"Is the fifth day of the week" )

#Copy this list to another new list
new_list = list_of_week_days.copy()
print("New List is", new_list)

#Merge both lists to first list
list_of_week_days.extend(new_list)
print(list_of_week_days)

#Clear all the items in the list
list_of_week_days.clear()
print(list_of_week_days)

#Print type of the list class
print(type(list_of_week_days))

