#!/usr/bin/env python3

num = int(input())

if num < 26:
    while num < 26:
        print(f"Inside the loop, my variable is {num}")
        num += 1
else:
    print("Error")