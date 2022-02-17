#!/usr/local/bin/python3
import sys

for line in sys.stdin:
    print(line.strip())
    (curV, otherV, weights) = line.strip().split('\t')
    if otherV[0] == "P":
        otherV = otherV.strip('P').strip('[').strip(']').split(',')
        weights = weights.strip('{').strip('}').split(',')
        for i in otherV:
            val = i.strip().strip('\'')
            print(f'{val}\t1\t{weights[0]}')

