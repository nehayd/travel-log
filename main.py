travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
list_of_values = []
for elements in travel_log:
  for values in elements.values():
    list_of_values.append(values)

add_this_country = {}
def add_new_country(country_name, visits_count, cities_visited):
  if country_name not in list_of_values:
    add_this_country["country"] = country_name
    add_this_country["visits"] = visits_count
    add_this_country["cities_visited"] = cities_visited
    travel_log.append(add_this_country)
  else:
    print("Data already present in the log.")


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# add_new_country("France", 12, ["Paris", "Lille", "Dijon"])
print(travel_log)



