#!/usr/local/bin/python3

import sys

mSum = 0
fSum = 0

for line in sys.stdin:
    (gender, value) = line.strip().split("\t")
    if gender == "male":
        mSum += (int)(value)
    else:
        fSum += (int)(value)
print(f'male:\t{mSum}')
print(f'female:\t{fSum}')
