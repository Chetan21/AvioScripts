import os


def temp(self):
    path = '/Users/Chetan/Desktop/test/test.csv'
    print path.split("/").__len__()
    print os.path.dirname(os.path.abspath(path))
    print os.path.dirname(path)
temp("")