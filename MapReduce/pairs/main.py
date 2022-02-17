import contextlib
import pyhdfs


fs = pyhdfs.HdfsClient(hosts='localhost:9870', user_name='evgenii')


def get_data():
    with contextlib.closing(fs.open('/MapReduce/output/pairs/part-00000')) as f:
        data = f.readlines()
    return data


def recommended(product, products):
    for i in products:
        t = i.split(', ')
        if product == t[0] and int(products[i]) > 4:
            print(t[1])



def main():
    data = get_data()
    product = input("Enter product:")
    products = {}
    for line in data:
        t = line.decode().split('\t')
        products[t[0]] = t[1]
    recommended(product,products)
    return 0


if __name__ == '__main__':
    main()