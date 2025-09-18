#!/usr/bin/env python3
def famous_births(name):
    items = list(name.items())
    sorted_items = sorted(items, key=lambda item: int(item[1]["date_of_birth"]))
    for key, value in sorted_items:
        name = value["name"]
        year = value["date_of_birth"]
        print(name + " is a great scientist born in " + year + ".")

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)