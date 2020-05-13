import ast

with open("treasure-random", "r") as fd:
    lines = fd.readlines()
    for line in lines:
        print('"{}",'.format(line.strip()))
