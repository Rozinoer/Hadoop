#!/usr/local/bin/python3
import sys

(auth, hub) = (0, 0)

for line in sys.stdin:
    print(line.strip())
    (index, parents, weigth) = line.strip().split('\t')
    weigth = weigth.strip('{').strip('}').split(',')
    (auth, hub) = (auth + float(weigth[0]), hub + float(weigth[1]))
print(f'{-1}\t{auth}')