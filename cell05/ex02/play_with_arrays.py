#!/usr/bin/env python3
org = [2, 8, 9, 48, 8, 22, -12, 2]
new = []

for i in org:
    if i > 5:
        new.append(i + 2)
    
print(f"{org}\n{new}")