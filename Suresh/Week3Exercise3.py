countries_population = {"India": "1.3", "China": "1.4", "USA": "0.32", "Indonesia": "0.26"}

def add_country(country_name, value):
    if country_name in countries_population.keys():
        print("Country Name Exists")
    else:
        countries_population.update({country_name:value})

def country_population(country_name):
    if country_name in countries_population.keys():
        return countries_population.get(country_name)
    else:
        print ("Country not in the list")


add_country('Pakistan', '0.6')
country_population('India')
