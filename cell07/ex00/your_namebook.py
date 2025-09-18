#!/usr/bin/env python3
def array_of_names(per):
    ary = []
    for first, last in per.items():
        fullname = f"{first.capitalize()} {last.capitalize()}"
        ary.append(fullname)
    return ary

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))