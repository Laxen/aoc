import sys
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
import re

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    ret = []
    with open(input_file, "r") as f:
        for line in f:
            ret.append([x for x in line.strip()])
    return np.array(ret)

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

rows, cols = np.where(data == "#")

addition = 1000000
s = 0
for i in range(len(rows)):
    row_a, col_a = rows[i], cols[i]
    for n in range(i+1, len(rows)):
        row_b, col_b = rows[n], cols[n]
        dist = abs(row_a - row_b) + abs(col_a - col_b)

        for y in range(row_a, row_b+1):
            if "#" not in data[y]:
                dist += addition - 1
        for x in range(min(col_a, col_b), max(col_a+1, col_b+1)):
            if "#" not in data[:,x]:
                dist += addition - 1

        s += dist

print(s)
assert s == 678626199476
