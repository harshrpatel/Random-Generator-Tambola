import ast

with open("goa-random", "r") as fd:
    lines = fd.readlines()
    for line in lines:
        print('"{}",'.format(line.strip()))
