import ast

with open("musical-random", "r") as fd:
    lines = fd.readlines()
    for line in lines:
        print('"{}",'.format(line.split('(')[0].strip()))
