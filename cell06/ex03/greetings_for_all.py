#!/usr/bin/env python3
def greetings(txt="noble stranger"):
    if type(txt) == str:
        print(f"Hello, {txt}")
    else:
        print("Error! It was not a name.")
        
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)