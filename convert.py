import ast

with open("biggboss.txt", "r") as fd:
    lines = fd.readlines()
    for line in lines:
        print('"{}",'.format(line.strip()))
