import os

def get_path(root_file, filename):
    root_path = os.path.dirname(os.path.realpath(root_file))
    return root_path + "/data/" + filename
