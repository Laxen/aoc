import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser

np.set_printoptions(linewidth=np.inf)
sys.setrecursionlimit(20000)

def make_data(input_file):
    ret = []
    with open(input_file, "r") as f:
        for line in f:
            ret.append([x for x in line.strip()])
    return ret

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

downs = ["|", "J", "L"]
ups = ["|", "7", "F"]
lefts = ["L", "F", "-"]
rights = ["-", "J", "7"]

paths = []

def build(node, path):
    if node[0] < 0 or node[0] >= len(data):
        return
    if node[1] < 0 or node[1] >= len(data[0]):
        return

    # time.sleep(0.1)
    # if node in path:
    #     exit()

    dy, dx = 0, 0
    if data[node[0]][node[1]] != "S":
        dy = node[0] - path[-1][0]
        dx = node[1] - path[-1][1]

    print(data[node[0]][node[1]], node, (dy, dx))
    match data[node[0]][node[1]]:
        case "|":
            if dx != 0:
                print("wrong")
                return
            build((node[0]+dy, node[1]), path + [node])
        case "-":
            if dy != 0:
                print("wrong")
                return
            build((node[0], node[1]+dx), path + [node])
        case "L":
            if dx != -1 and dy != 1:
                print("wrong")
                return
            build((node[0]+dx, node[1]+dy), path + [node])
        case "J":
            if dx != 1 and dy != 1:
                print("wrong")
                return
            build((node[0]-dx, node[1]-dy), path + [node])
        case "F":
            if dx != -1 and dy != -1:
                print("wrong")
                return
            build((node[0]-dx, node[1]-dy), path + [node])
        case "7":
            if dx != 1 and dy != -1:
                print("wrong")
                return
            build((node[0]+dx, node[1]+dy), path + [node])
        case "S":
            if len(path) > 0:
                # Returned to S
                paths.append(path)
                return

            build((node[0], node[1]-1), path + [node])
            build((node[0]+1, node[1]), path + [node])
            build((node[0], node[1]+1), path + [node])
            build((node[0]-1, node[1]), path + [node])
        case ".":
            return

start = None
for y, row in enumerate(data):
    for x, col in enumerate(row):
        if col == "S":
            start = (y, x)
            break
    if start is not None:
        break

build(start, [])
print(paths)
print(len(paths[0])//2)
