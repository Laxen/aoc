import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
from pprint import pprint
from functools import lru_cache

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    ret = []
    with open(input_file, "r") as f:
        for l in f:
            ret.append([x for x in l.strip()])
    return np.array(ret)

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
    max_steps = 64
else:
    print("EXAMPLE\n")
    data = make_data("example")
    max_steps = 6

# -----------------

def walk(start, steps):
    visited = visited_even if steps % 2 == 0 else visited_odd
    if start in visited:
        if visited[start] <= steps:
            return []
    visited[start] = steps

    if steps == max_steps:
        return [start]

    ret = []

    for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        new = (start[0] + x, start[1] + y)
        if new[0] < 0 or new[1] < 0:
            continue
        try:
            if data[new] == "#":
                continue
            ret.extend(walk(new, steps + 1))
        except IndexError:
            continue

    return ret

#max_steps = 6
visited_even = dict()
visited_odd = dict()
start = None
for c, v in np.ndenumerate(data):
    if v == "S":
        start = c
        break

tiles = walk(start, 0)
print(len(set(tiles)))
print(len(visited_even), len(visited_odd))

# for t in visited_even:
#     data[t] = "O"
# for l in data:
#     print("".join(l))
