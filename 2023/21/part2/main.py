import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser, in_bounds
from pprint import pprint
from functools import lru_cache

np.set_printoptions(linewidth=np.inf)
sys.setrecursionlimit(10000)

def make_data(input_file):
    ret = []
    with open(input_file, "r") as f:
        for l in f:
            ret.append([x for x in l.strip()])
    return np.array(ret)

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
    max_steps = 65 + 131 * 3
    print(max_steps)
else:
    print("EXAMPLE\n")
    data = make_data("example")
    max_steps = 100
    print("max_steps", max_steps)

# -----------------

def walk(start, steps, max_steps):
    visited = visited_even if steps % 2 == 0 else visited_odd
    if start in visited:
        if visited[start] <= steps:
            return []
    visited[start] = steps

    if steps == max_steps:
        return

    for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        new_big = (start[0] + x, start[1] + y)
        new = (new_big[0] % data.shape[0], new_big[1] % data.shape[1])
        if data[new] == "#":
            continue
        walk(new_big, steps + 1, max_steps)

S = (None, None)
for c, v in np.ndenumerate(data):
    if v == "S":
        S = c
        break

visited_even = {}
visited_odd = {}
walk(S, 0, 65)
a = len(visited_odd)

visited_even = {}
visited_odd = {}
walk(S, 0, 65 + 131)
b = len(visited_even)

visited_even = {}
visited_odd = {}
walk(S, 0, 65 + 131*2)
c = len(visited_odd)

print(a, b, c)
# Pop it into Wolfram Alpha quadratic fit calculator, then run it with 202300
# as x to get answer
