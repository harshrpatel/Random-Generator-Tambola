import ast

with open("tvshows-random", "r") as fd:
    lines = fd.readlines()
    for line in lines:
        print('"{}",'.format(line.strip()))
