import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser, in_bounds
from pprint import pprint

np.set_printoptions(linewidth=np.inf, threshold=np.inf)

def make_data(input_file):
    ret = []
    with open(input_file, "r") as f:
        for line in f:
            direction, distance, color = line.strip().split(" ")

            distance = color[2:2+5]
            match color[-2]:
                case "0":
                    direction = "R"
                case "1":
                    direction = "D"
                case "2":
                    direction = "L"
                case "3":
                    direction = "U"

            ret.append((direction, int(distance, 16)))
    return ret

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

s = 1
pos = (0, 0)

for direction, distance in data:
    print(pos, direction, distance, end=" ")

    if direction == "R":
        s += distance
        pos = (pos[0], pos[1] + distance)
    elif direction == "L":
        pos = (pos[0], pos[1] - distance)
    elif direction == "U":
        s -= pos[1] * distance
        pos = (pos[0] - distance, pos[1])
    elif direction == "D":
        s += (pos[1] + 1) * distance
        pos = (pos[0] + distance, pos[1])

    print(s)

print(s)
