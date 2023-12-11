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

new_data = data.copy()
count =  0
for i, row in enumerate(data):
    if "#" not in row:
        count += 1
        new_data = np.insert(new_data, i+count, np.array(["." for _ in range(len(row))]), axis=0)

count = 0
data = new_data.copy()
for i, col in enumerate(data.T):
    if "#" not in col:
        count += 1
        new_data = np.insert(new_data, i+count, np.array(["." for _ in range(len(col))]), axis=1)

data = new_data.copy()

rows, cols = np.where(data == "#")

s = 0
for i in range(len(rows)):
    row_a, col_a = rows[i], cols[i]
    for n in range(i+1, len(rows)):
        row_b, col_b = rows[n], cols[n]
        dist = abs(row_a - row_b) + abs(col_a - col_b)
        s += dist

print(s)
