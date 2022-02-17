#!/usr/bin/python3

import sys

for line in sys.stdin:
    for i in line.strip().split(" "):
        print(i, end='\t')
        for j in line.strip().split(" "):
            if i != j:
                print(j, end=', ',sep=', ')
        print('')