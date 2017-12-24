import os
import sys

# Update sys path in order to resolve module imports from this project itself
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#def get_path(root_file, filename):
#    root_path = os.path.dirname(os.path.realpath(root_file))
#    return root_path + "/../data/" + filename

def get_path(filename):
    root_path = os.path.dirname(os.path.realpath(__file__))
    return root_path + "/../data/" + filename
