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

sum = 0
for row in data:
    mi = min(row)
    ma = max(row)
    print(ma, mi)
    sum += ma-mi

print(sum)
