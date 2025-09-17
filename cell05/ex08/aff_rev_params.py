#!/usr/bin/env python3
import sys

if len(sys.argv) > 2:
    for i in (reversed(sys.argv[1:])):
        print(i)
else:
    print("none")