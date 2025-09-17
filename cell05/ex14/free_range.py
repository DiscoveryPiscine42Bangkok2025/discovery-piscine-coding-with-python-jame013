#!/usr/bin/env python3
import sys
result = []

if len(sys.argv) == 3:
    for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        result.append(i)
    print(result)
else:
    print("none")