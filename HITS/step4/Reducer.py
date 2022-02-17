#!/usr/local/bin/python3
import sys

(g_auth, g_hub) = (0, 0)

for line in sys.stdin:
    tmp = line.strip().split('\t')
    if tmp[0] == "-1":
        (fV, sV, p) = line.strip().split('\t')
        (g_auth, g_hub) = (float(sV), float(p))
    else:
        (fV, weight) = line.strip().split('\t')
        weight = weight.strip('{').strip('}').split(',')
        print(f'{fV}\t', "{:.3f}".format(float(weight[0]) / g_auth), "\t{:.3f}".format(float(weight[1]) / g_hub))
