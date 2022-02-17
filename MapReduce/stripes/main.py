import contextlib
import pyhdfs
from requests.api import patch

fs = pyhdfs.HdfsClient(hosts='localhost:9870', user_name='evgenii')


def get_data():
    with contextlib.closing(fs.open('/MapReduce/output/stripes/part-00000')) as f:
        data = f.readlines()
    return data


def recommended(products):
    arr = products.split(' ')
    arr.pop()
    for item in arr:
        (key, value) = item.split(':')
        if int(value) > 4:
            print(key)


def main():
    data = get_data()
    product = input("Enter product:")
    for line in data:
        t = line.decode().split('\t')
        if product == t[0]:
            recommended(t[1])
    return 0


if __name__ == '__main__':
    main()
