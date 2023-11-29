import sys
import numpy as np
from collections import defaultdict
from pyhelpers import Parser

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    return Parser.ints_to_list(input_file)

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

def manhattan(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

coords = dict()
themap = dict()

xmax = 0
ymax = 0

for i in range(1, len(data), 2):
    coords[(data[i-1], data[i])] = i
    themap[(data[i-1], data[i])] = i
    xmax = max(data[i-1], xmax)
    ymax = max(data[i], ymax)

dists = dict()
for x in range(0, xmax+1):
    for y in range(0, ymax+1):
        val = None
        dist = 0
        for c, v in coords.items():
            dist += manhattan((x, y), c)
            if dist >= 10000:
                break
        else:
            dists[(x, y)] = dist

print(len(dists))
