import os

def create_dir(directory):
    if not os.path.exist(directory):
        os.makedirs(directory)

def write_file(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()