import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
from pprint import pprint

np.set_printoptions(linewidth=np.inf)
sys.setrecursionlimit(20000)

def make_data(input_file):
    ret = []
    with open(input_file, "r") as f:
        for line in f:
            ret.append(list(line.strip()))
    return ret

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def traverse(start, direction):
    if start[0] < 0 or start[1] < 0 or start[0] >= len(data) or start[1] >= len(data[0]):
        return

    if start in energized:
        if direction in energized[start]:
            return
    energized[start].append(direction)

    tile = data[start[0]][start[1]]
    match tile:
        case ".":
            traverse(add(start, direction), direction)
        case "/":
            new_direction = (-direction[1], -direction[0])
            traverse(add(start, new_direction), new_direction)
        case "\\":
            new_direction = (direction[1], direction[0])
            traverse(add(start, new_direction), new_direction)
        case "|":
            if direction[0] == 0:
                traverse(add(start, (-1, 0)), (-1, 0))
                traverse(add(start, (1, 0)), (1, 0))
            else:
                traverse(add(start, direction), direction)
        case "-":
            if direction[1] == 0:
                traverse(add(start, (0, -1)), (0, -1))
                traverse(add(start, (0, 1)), (0, 1))
            else:
                traverse(add(start, direction), direction)

energized = defaultdict(list)
maximum = 0

# Top and bottom
for i in range(len(data[0]) - 1):
    traverse((0, i), (1, 0))
    maximum = max(maximum, len(energized))
    energized.clear()
    traverse((len(data) - 1, i), (-1, 0))
    maximum = max(maximum, len(energized))
    energized.clear()

# Right and left
for i in range(len(data) - 1):
    traverse((i, len(data[0]) - 1), (0, -1))
    maximum = max(maximum, len(energized))
    energized.clear()
    traverse((i, 0), (0, 1))
    maximum = max(maximum, len(energized))
    energized.clear()

print(maximum)
