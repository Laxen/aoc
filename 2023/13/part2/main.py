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

def fold(pattern, avoid):
    for i in range(1, len(pattern)):
        if i == avoid:
            continue

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

def smudge(pattern, initial):
    for y in range(len(pattern)):
        for x in range(len(pattern[y])):
            pattern[y,x] = "#" if pattern[y,x] == "." else "."

            avoid = int(initial[1:])

            row = fold(pattern, avoid if "H" in initial else None)
            if row and "H" + str(row) != initial:
                return 100 * row

            col = fold(pattern.T, avoid)
            if col and "V" + str(col) != initial:
                return col

            pattern[y,x] = "#" if pattern[y,x] == "." else "."
    raise Exception("No smudge found")

s = 0

for pattern in data:
    initial = None

    row = fold(pattern, None)
    if row:
        initial = "H" + str(row)

    if not initial:
        col = fold(pattern.T, None)
        if col:
            initial = "V" + str(col)

    s += smudge(pattern, initial)

print(s)

assert s == 24847 or s == 400
