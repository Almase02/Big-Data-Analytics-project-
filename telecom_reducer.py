#!/usr/bin/env python3
import sys

current_key = None
current_total = 0

for line in sys.stdin:
    key, value = line.strip().split("\t")

    if "." in value:
        value = float(value)
    else:
        value = int(value)

    if current_key == key:
        current_total += value
    else:
        if current_key:
            print(current_key + "\t" + str(current_total))
        current_key = key
        current_total = value

if current_key:
    print(current_key + "\t" + str(current_total))
