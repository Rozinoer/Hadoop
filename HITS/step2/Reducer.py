#!/usr/local/bin/python3
import sys

(g_auth, g_hub) = (0., 0.)


for line in sys.stdin:
    tmp = line.strip().split('\t')
    if tmp[0] == "-1":
        (fV, sV) = line.strip().split('\t')
        (g_auth, g_hub) = (float(sV), 0)
    else:
        weight = tmp[2]
        weight = weight.strip('{').strip('}').split(',')
        # print(f'{fV}\t', "{:.3f}".format(float(weight[0]) / g_auth), "\t\t{:.3f}".format(float(weight[1]) / g_hub))
        if g_auth > 0:
            print(f'{tmp[0]}\t{tmp[1]}\t{{',"{:.3f},".format(float(weight[0]) / g_auth), f'{weight[1]}}}')
        else:
            print(f'{tmp[0]}\t{tmp[1]}\t{{',"{:.3f},".format(weight[0], f'{weight[1]}}}'))
