from os import listdir
from os.path import isdir, join

def walk_directory(d, indent):
    for f in listdir(d):
        print(indent + f)
        if isdir(join(d, f)):
            walk_directory(join(d, f), 2 * indent)

# '.' means current directory
walk_directory('Desktop', ' ')
