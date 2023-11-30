import sys
import numpy as np
from collections import defaultdict
from pyhelpers import Parser

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    with open(input_file, "r") as f:
        ret = []
        for line in f:
            s = line.strip().split("\t")
            ret.append([int(x) for x in s])
        return ret

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

def handle(row):
    for i1 in range(0, len(row) - 1):
        for i2 in range(i1+1, len(row)):
            x1 = row[i1]
            x2 = row[i2]

            if x1 == 0 or x2 == 0:
                continue

            if x1 % x2 == 0:
                return x1/x2
            elif x2 % x1 == 0:
                return x2/x1
    exit()

sum = 0
for row in data:
    sum += handle(row)

print(sum)
