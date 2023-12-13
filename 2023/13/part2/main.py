import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
from pprint import pprint

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    ret = []
    ret.append([])
    with open(input_file, "r") as f:
        for line in f:
            if line.strip() == "":
                ret.append([])
            else:
                element = line.strip()
                ret[-1].append(list(element))
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

        top = pattern[:i]
        bottom = pattern[i:]
        bottom.reverse()

        # print(i, "top")
        # pprint(top)
        # print(i, "bottom")
        # pprint(bottom)
        # print(i, "bottom[:i]")
        # pprint(bottom[:i])
        # print()

        if len(top) > len(bottom):
            if top[len(top) - len(bottom):] == bottom:
                return i
        else:
            if top == bottom[len(bottom) - len(top):]:
                return i

    return None

def smudge(pattern, initial, s):
    for y in range(len(pattern)):
        for x in range(len(pattern[y])):
            if pattern[y][x] == "#":
                pattern[y][x] = "."
            else:
                pattern[y][x] = "#"

            avoid = None
            if initial[0] == "H":
                avoid = int(initial[1:])

            row = fold(pattern, avoid)
            if row and "H" + str(row) != initial:
                s = 100 * row
                print("H" + str(row), y, x)
                return s

            avoid = None
            if initial[0] == "V":
                avoid = int(initial[1:])

            pattern = list(map(list, zip(*pattern)))
            col = fold(pattern, int(initial[1:]))
            if col and "V" + str(col) != initial:
                s = col
                print("V" + str(col), y, x)
                return s

            pattern = list(map(list, zip(*pattern)))

            if pattern[y][x] == "#":
                pattern[y][x] = "."
            else:
                pattern[y][x] = "#"

    pprint(pattern)
    raise Exception("No smudge found")

s = 0

for pattern in data:
    initial = None

    row = fold(pattern, None)
    if row:
        initial = "H" + str(row)

    if not initial:
        pattern = list(map(list, zip(*pattern)))
        col = fold(pattern, None)
        if col:
            initial = "V" + str(col)
        pattern = list(map(list, zip(*pattern)))

    if not initial:
        raise Exception("No fold found")

    print("initial", initial)
    s += smudge(pattern, initial, s)

print(s)
