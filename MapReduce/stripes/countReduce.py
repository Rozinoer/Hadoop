#!/usr/bin/python3
import sys
from collections import defaultdict

lastKey = None
d = defaultdict(int)

for line in sys.stdin:
    (key, values) = line.strip(',').split("\t")
    products = values.split(', ')
    if lastKey and lastKey != key:
        print(lastKey, end='\t')
        for i in d:
            print(f'{i}:{d[i]}',end=' ')
        print('')
        d.clear()
        lastKey = key
    else:
        lastKey = key
    for item in products:
        d[item] += 1
if lastKey:
    print(lastKey, end='\t')
    for key in d:
        print(f'{key}:{d[key]}',end=' ')
    print('')

