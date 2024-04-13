# # Create a dictionary describing you in as much detail as possible(no bank accounts, but you get the idea).
# Make sure to start from basic key: value pairs and go to deep nesting where value would be at least a list of
# dictionaries.
import json
me = {
    "first_name": "Triinu",
    "last_name": "Niklus",
    "age": "27",
    "birth_date": "1996-08-22",
    "gender": "female",
    "email": "triinu.niklus@gmail.com",
    "country": "Estonia",
    "city": "Tartu",
    "kids":[{"name": "Marken",
            "age": 7},
        {"name": "Mariliis",
            "age": 0.5 },],
    "dogs": ["Dominic", "V2lk"],
    "cat": "Sammy"}
print(me)
me['favorite_color'] = "Black","Red", "Blue"
me['favorite_food'] = "Burgers"
me['hobbies'] = "Knitting"
print(json.dumps(me, indent= 3))