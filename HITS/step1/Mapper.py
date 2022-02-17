#!/usr/local/bin/python3
import sys

for line in sys.stdin:
    print(line.strip())
    (curV, children, weights) = line.strip().split('\t')
    if children != "NO":
        weights = weights.strip('{').strip('}').split(',')
        for child in children.strip('[').strip(']').split(','):
            print(f'{child}\t{weights[0]}\t{curV}')
