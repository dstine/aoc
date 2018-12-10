import os

def get_path(filename):
    root_path = os.path.dirname(os.path.realpath(__file__))
    return root_path + "/../../data/" + filename
