import sys
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
import re

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    with open(input_file, "r") as f:
        ret = [list(line.strip()) for line in f.readlines()]
    return np.array(ret)

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

num = ""
ispartnum = False
oknums = []

for rowi, row in enumerate(data):
    for coli, col in enumerate(row):
        if col.isnumeric():
            num += col
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if (dy, dx) == (0, 0):
                        continue

                    if rowi + dy < 0 or rowi + dy >= data.shape[0] \
                            or coli + dx < 0 or coli + dx >= data.shape[1]:
                        continue

                    if data[rowi+dy][coli+dx] != "." and not data[rowi+dy][coli+dx].isnumeric():
                        ispartnum = True

        if not col.isnumeric() or coli == data.shape[1] - 1:
            if num != "" and ispartnum:
                oknums.append(int(num))
            num = ""
            ispartnum = False

print(sum(oknums))
