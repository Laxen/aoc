import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser, in_bounds
from pprint import pprint

np.set_printoptions(linewidth=np.inf)
sys.setrecursionlimit(10000)

def make_data(input_file):
    ret = []
    with open(input_file, "r") as f:
        for line in f:
            ret.append(list(line.strip()))
    return np.array(ret)

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

def walk(y, x, visited):
    if not in_bounds((y, x), data):
        return

    if data[y, x] == "#":
        return

    if (y, x) in visited:
        return

    if (y, x) == end:
        print("Found end")
        hikes.append(visited)
        return

    if data[y, x] == ".":
        walk(y+1, x, visited + [(y, x)])
        walk(y-1, x, visited + [(y, x)])
        walk(y, x+1, visited + [(y, x)])
        walk(y, x-1, visited + [(y, x)])
    elif data[y, x] == ">":
        walk(y, x+1, visited + [(y, x)])
    elif data[y, x] == "<":
        walk(y, x-1, visited + [(y, x)])
    elif data[y, x] == "^":
        walk(y-1, x, visited + [(y, x)])
    elif data[y, x] == "v":
        walk(y+1, x, visited + [(y, x)])
    else:
        raise Exception("Unknown char", data[y, x])

start = (-1, -1)
end = (-1, -1)
for i, c in enumerate(data[0]):
    if c == ".":
        start = (0, i)
        break
for i, c in enumerate(data[-1]):
    if c == ".":
        end = (len(data)-1, i)
        break
print(start, "->", end)

hikes = []
visited = []
walk(*start, visited)

max_len = max(len(h) for h in hikes)
print("Max len", max_len)
# for y, x in hikes[0]:
#     data[y, x] = "O"
# for row in data:
#     print(" ".join(row))
