import ast

with open("cartoon-random.txt", "r") as fd:
    lines = fd.readlines()
    for line in lines:
        print('"{}",'.format(line.strip()))
