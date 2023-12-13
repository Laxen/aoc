import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pprint import pprint

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    ret = []
    with open(input_file, "r") as f:
        miniret = []
        for line in f:
            if line.strip() == "":
                ret.append(np.array(miniret))
                miniret = []
            else:
                element = line.strip()
                miniret.append(list(element))
    ret.append(np.array(miniret))
    return ret

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

def fold(pattern):
    for i in range(1, len(pattern)):
        top = pattern[:i,:]
        bottom = pattern[i:,:]
        bottom = np.flipud(bottom)

        if len(top) > len(bottom):
            if np.all(top[-len(bottom):,:] == bottom):
                return i
        else:
            if np.all(top == bottom[-len(top):,:]):
                return i

    return None

s = 0

print("Horizontal")
for pattern in data:
    row = fold(pattern)
    s += 100 * row if row else 0

print("Vertical")
for pattern in data:
    col = fold(pattern.T)
    s += col if col else 0

print(s)
