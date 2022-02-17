#!/usr/local/bin/python3
import sys

(V, index, hub) = (None, 0, 0)

for line in sys.stdin:
    (curV, otherV, weigth) = line.strip().split('\t')
    V = curV
    if otherV == "1":
        auth = 1
        hub += float(weigth.strip())
    else:
        if V == curV:
            weigth = weigth.strip('{').strip('}').split(',')
            print(f'{curV}\t'
            +'{' + f'{float(weigth[0])},{float(weigth[1]) + float(hub)}' + '}')
        else:
            print(f'{curV}\r{weigth}')
        (V, index, hub) = (None, 0, 0)