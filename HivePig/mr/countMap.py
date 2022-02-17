#!/usr/local/bin/python3

import sys
import pyhdfs
import contextlib

def get_data():
    fs = pyhdfs.HdfsClient(hosts='localhost:9870', user_name='evgenii')
    with contextlib.closing(fs.open('/user/hive/warehouse/customerdata/customerData.txt')) as f:
        data = f.readlines()
        return data

for lines in sys.stdin:
    (user, value, month, bank) = lines.strip().split(',')
    for line in get_data():
        (userId, gender, age, married) = line.decode().strip().split(',')
        if user == userId:
            print(f'{gender}\t{value}')