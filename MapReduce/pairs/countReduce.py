#!/usr/bin/python3
import sys

(fKey, sKey, sum)=(None, None, 0)

for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    (newF, newS) = key.split(', ')
    if fKey and (newF != fKey or newS != sKey):
        print(f'{fKey}, {sKey}\t{sum}')
        (fKey, sKey, sum)=(newF, newS, 1)
    else:
        (fKey, sKey, sum) = (newF, newS, sum + 1)

if fKey:
    print(f'{fKey}, {sKey}\t{sum}')


