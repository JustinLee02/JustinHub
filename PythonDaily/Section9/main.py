# dictionary : {Key1: Value1, Key2: Value2, ...}


my_dict = {
    "Key1": "Value1",
    "Key2": "Value2",
}

# printing Value
print(my_dict["Key1"])

# Adding new items
my_dict["Key3"] = "Value3"

print(my_dict)

# Wipe an existing dictionary
# my_dict = {}
# print(my_dict)

# Edit an item in a dictionary
my_dict["Key3"] = "NewValue3"
print(my_dict)

# for loop
for thing in my_dict:
    print(thing) # Just printing keys
    print(my_dict[thing])

# Nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Nice", "Lille"],
    "USA": ["NY", "LA", "Chicago"],
}

# Nesting a dictionary in a dictionary

travel_log_2 = [
    {
        "country": "France",
        "cities_Visited": ["Paris", "Nice", "Lille"],
        "total_Visits": 12
    },
    {
        "country": "America",
        "cities_Visited": ["NY", "LA", "Chicago"],
        "total_Visits": 1
    },
]
