import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser, in_bounds
from pprint import pprint
from heapq import heappush, heappop

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    ret = []
    with open(input_file, "r") as f:
        for line in f:
            ret.append([int(x) for x in list(line.strip())])
    return np.array(ret)

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

def turnleft(heading):
    return (-heading[1], heading[0])

def turnright(heading):
    return (heading[1], -heading[0])

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def path(start):
    queue = []
    heappush(queue, (0, start, (0, 1), -1)) # dist, pos, heading, steps
    visited = set()

    while queue:
        dist, pos, heading, steps = heappop(queue)

        if pos == (data.shape[0] - 1, data.shape[1] - 1):
            return dist

        if (pos, heading, steps) in visited:
            continue
        visited.add((pos, heading, steps))

        # Straight
        new_pos = add(pos, heading)
        if steps < (3 - 1): # First step is 0, hence <. We need room for 1 more step to continue, hence -1.
            if in_bounds(new_pos, data):
                heappush(queue, (dist + data[new_pos], new_pos, heading, steps + 1))

        # Left
        new_pos = add(pos, turnleft(heading))
        if in_bounds(new_pos, data):
            heappush(queue, (dist + data[new_pos], new_pos, turnleft(heading), 0))

        # Right
        new_pos = add(pos, turnright(heading))
        if in_bounds(new_pos, data):
            heappush(queue, (dist + data[new_pos], new_pos, turnright(heading), 0))

    return None

dist = path((0, 0))
print(dist)
