from pywebhdfs.errors import *
from pywebhdfs.webhdfs import PyWebHdfsClient

current_dir = "localhost:9870"


def current_directory():
    i = len(current_dir) + 10
    arr = '*' * i
    print("\033[32m")
    print(arr)
    print("*    {}    *".format(current_dir))
    print(arr)
    print("\033[0m")


def create_file(hdfs_client, data):
    arr = current_dir.split("/")
    name = data.split('/')
    i = len(arr)
    j = 1
    if len(arr) > 1:
        new_path = arr[j]
        while j < i:
            new_path.join(arr[j])
            new_path.join("/")
            j += 1
        new_path += "/"
    else:
        new_path = ''
    try:
        f = open(data, mode='r')
        hdfs_client.create_file(path=new_path + name[len(name) - 1], file_data=f.read())
    except FileNotFound:
        print("File not found..")
    return 0


def create_dir(hdfs_client, path):
    arr = current_dir.split("/")
    i = len(arr)
    j = 1
    if len(arr) > 1:
        new_path = arr[j]
        while j < i:
            new_path.join(arr[j])
            new_path.join("/")
            j += 1
        new_path += "/" + path
    else:
        new_path = path
    try:
        hdfs_client.make_dir(path=new_path)
    except FileNotFound:
        print('File not found..')
    print('Create..')
    return 0


def append_file(hdfs_client, path):
    data = input("Enter the local file path with data: ")
    try:
        f = open(data, mode='r')
        hdfs_client.append_file(path=path, file_data=f.read())
    except FileNotFound:
        print("File not found")
    print('Append..')
    return 0


def delete_file_dir(hdfs_client, path):
    hdfs_client.delete_file_dir(path=path)
    print("Delete..\n")
    return 0


def get_status(hdfs_client, path):
    try:
        data = (hdfs_client.read_file(path=path))
        file = open("/Users/evgenii/Desktop/PyCharm/hdfsManager/test", "wb")
        file.write(data)
    except FileNotFound:
        print("File not found")
    return 0


def list_dir(hdfs_client):
    arr = current_dir.split("/")
    i = len(arr)
    j = 1
    if len(arr) > 1:
        new_path = arr[j]
        while j < i:
            new_path.join(arr[j])
            new_path.join("/")
            j += 1
    else:
        new_path = "./"
    x = hdfs_client.list_dir(path=new_path)
    print(x)
    return 0


def read(hdfs_client):
    print("Read\n")
    path = input("{}/".format(current_dir))
    hdfs_client.make_dir(path=path)
    return 0


def rename(hdfs_client):
    print("Rename\n")
    current_name = input("{}/".format(current_dir))
    dist_name = input("Enter the new file path name: ")

    hdfs_client.rename_file_dir(current_name, dist_name)
    return 0


def change_dir(hdfs_client, path):
    global current_dir
    new_path = ""
    if not path == "..":
        try:
            arr = current_dir.split("/")
            for i in arr:
                if arr.index(i) != 0:
                    new_path += i + "/"
            x = hdfs_client.get_file_dir_status(path=new_path + path)
        except FileNotFound:
            print("Dir not found..")
        current_dir = '/'.join([current_dir, path])
    else:
        try:
            arr = current_dir.split("/")
            for i in arr:
                if arr.index(i) != 0 and arr.index(i) != len(arr) - 1:
                    new_path += i + "/"
            new_path = new_path.rstrip('/')
            x = hdfs_client.get_file_dir_status(path=new_path)
            current_dir = "localhost:9870/" + new_path
        except ValueError:
            print("Dir not found..")


def start(hdfs_client):
    while 1:
        current_directory()
        action = input()
        var = action.split(' ')
        if var[0] == 'put':
            create_file(hdfs_client=hdfs_client, data=var[1])
        elif var[0] == 'mkdir':
            create_dir(hdfs_client=hdfs_client, path=var[1])
        elif var[0] == 'append':
            append_file(hdfs_client=hdfs_client, path=var[1])
        elif var[0] == 'delete':
            delete_file_dir(hdfs_client=hdfs_client, path=var[1])
        elif var[0] == 'get':
            get_status(hdfs_client=hdfs_client, path=var[1])
        elif var[0] == 'ls' or var[0] == "lls":
            list_dir(hdfs_client=hdfs_client)
        elif var[0] == 'cd':
            change_dir(hdfs_client=hdfs_client, path=var[1])
        else:
            print("Wrong command:", var)


def init_user():
    # host = input("Host: ")
    # port = input("Port: ")
    # user_name = input("User name: ")
    web = PyWebHdfsClient(host="localhost", port=9870, user_name="evgenii")
    return web


def main():
    hdfs = init_user()
    start(hdfs_client=hdfs)
    return 0


if __name__ == '__main__':
    main()
