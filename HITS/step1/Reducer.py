#!/usr/local/bin/python3
import sys

(V, auth, parents) = (None, 0, [])

for line in sys.stdin:
    (curV, otherV, weigth) = line.strip().split('\t')
    if otherV[0] != '[' and otherV != 'NO':
        auth += float(otherV)
        parents.append(weigth)
        V = curV
    else:
        if V == curV:
            weigth = weigth.strip('{').strip('}').split(',')
            print(f'{curV}\tP{parents}' + f'\t{{{float(weigth[0]) + float(auth)},{float(weigth[1])}' + '}')
        else:
            print(line.strip())
        (V, auth, parents) = (None, 0, [])