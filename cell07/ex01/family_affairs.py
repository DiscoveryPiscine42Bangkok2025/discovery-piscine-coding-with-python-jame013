#!/usr/bin/env python3
def find_the_redheads(fam):
    name = []
    for key, value in fam.items():
        if value == "red":
            name.append(key)
    return name
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))