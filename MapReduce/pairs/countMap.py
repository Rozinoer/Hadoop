#!/usr/bin/python3

import sys

for line in sys.stdin:
    for i in line.strip().split(" "):
        for j in line.strip().split(" "):
            if i != j:
                print("{}, {}\t1".format(i, j))
