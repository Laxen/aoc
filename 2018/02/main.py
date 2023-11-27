import sys
import numpy as np
from pyhelpers import Parser

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    with open(input_file, "r") as f:
        return f.readlines()

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

glob_twos = 0
glob_threes = 0

for l in data:
    l = l.strip()
    counts = dict()
    for c in l:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    twos = [key for key, val in counts.items() if val == 2]
    threes = [key for key, val in counts.items() if val == 3]

    if len(twos) > 0:
        glob_twos += 1
    if len(threes) > 0:
        glob_threes += 1

print(glob_twos * glob_threes)
