travel_log = [
    {
        "country" : "france",
        "visits" : 5,
        "cities" : ["paris", "lille", "dijon"],
    },
    {
        "country" : "germany",
        "visits" : 12,
        "cities" : ["berlin", "hamburg", "stuttgart"],
    },
]
def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersberg"])
print(travel_log)