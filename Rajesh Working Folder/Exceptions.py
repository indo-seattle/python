countries_population = {'India': '1.3'}

# As you saw earlier, when syntactically correct code runs into an error, Python will throw an exception error.
# This exception error will crash the program if it is unhandled.
# The except clause determines how your program responds to exceptions.


print('start')
try:
    if 'India' in countries_population.keys():
        raise Exception('The country already exists.')
except Exception as ve:
    print(ve)
finally:
    print('finally')

print('end')