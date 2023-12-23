import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser, in_bounds
from pprint import pprint
from heapq import heappush, heappop
from functools import lru_cache

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

def walk(y, x, visited, node, length):
    if not in_bounds((y, x), data):
        return

    if data[y, x] == "#":
        return

    if (y, x) == end:
        graph[node][(y, x)] = length
        return

    if (y, x) in visited:
        return

    n_directions = 0
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if in_bounds((y+dy, x+dx), data) and data[y+dy, x+dx] != "." and data[y+dy, x+dx] != "#":
            n_directions += 1

    if n_directions > 1:
        if (y, x) in graph[node]:
            return

        graph[node][(y, x)] = length
        graph[(y, x)][node] = length

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            walk(y+dy, x+dx, visited + [(y, x)], (y, x), 1)
    else:
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            walk(y+dy, x+dx, visited + [(y, x)], node, length + 1)

def walk_nodes(node, visited, length):
    if node == end:
        return length

    ret = 0
    for n in graph[node]:
        if n not in visited:
            ret = max(ret, walk_nodes(n, visited + [node], length + graph[node][n]))

    return ret

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

graph = defaultdict(dict)
visited = []
max_len = 0
walk(*start, visited, start, 0)

ret = walk_nodes(start, [], 0)

print(ret)
