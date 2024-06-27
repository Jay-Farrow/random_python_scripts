# Task: write a program that adds to a travel_log. You can see a travel which
# is a list that contains 2 dictionaries. Your job is to create a function that can add
# new contries to this list. 

country = input("Enter Country Name:\n")
visits = int(input("Enter the number of times visited:\n"))
string_of_cities = input("Enter the names of each city visited: (Separated by comma)\n")

list_of_cities = []
list_of_cities = string_of_cities.split(", ")

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    },
]

def add_new_country(country, visits, list_of_cities):
    add_country = {
        "country": country,
        "visits": visits,
        "cities": list_of_cities,
    }
    travel_log.append(add_country)

add_new_country(country=country, visits=visits, list_of_cities=list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favorite city was {travel_log[2]['cities'][0]}.")

# Another way of doing it.
'''
def add_new_country(country, visits, list_of_cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
'''