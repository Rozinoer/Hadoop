#!/usr/local/bin/python3
import sys

(key, auth, hub) = (None, None, None)


for line in sys.stdin:
    (newKey, newAuth, newHub) = line.strip().split("\t")
    if (newKey == key):
        print(f'{key}\t{newAuth}\t' + '{' + f'{auth.strip()},{hub}}}')
    else:
        (key, auth, hub) = (newKey, newAuth, newHub)
