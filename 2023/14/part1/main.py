import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
from pprint import pprint

np.set_printoptions(linewidth=np.inf)

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

def cycle():
    tilt(data, (-1, 0))
    tilt(data, (0, -1))
    tilt(data, (1, 0))
    tilt(data, (0, 1))

def tilt(data, direction):
    flip = None

    if direction == (1, 0):
        direction = (-1, 0)
        data = np.flipud(data)
        flip = "ud"
    elif direction == (0, 1):
        direction = (0, -1)
        data = np.fliplr(data)
        flip = "lr"

    for coord, val in np.ndenumerate(data):
        if val == "O":
            while True:
                new_coord = (coord[0] + direction[0], coord[1] + direction[1])

                if new_coord[0] >= data.shape[0] or new_coord[0] < 0:
                    break
                elif new_coord[1] >= data.shape[1] or new_coord[1] < 0:
                    break
                elif data[new_coord] == "#" or data[new_coord] == "O":
                    break

                data[new_coord] = "O"
                data[coord] = "."
                coord = new_coord

    if flip == "lr":
        data = np.fliplr(data)
    elif flip == "ud":
        data = np.flipud(data)

def load():
    s = 0
    for coord, val in np.ndenumerate(data):
        if val == "O":
            s += data.shape[0] - coord[0]
    return s

cache = set()

cycles = 1000000000
i = 1
while True:
    if i % 100 == 0:
        print(i)
    cycle()

    if i == 1000:
        s = str(data)
        cache.add(s)

    if str(data) in cache:
        print("found", i)
        i = cycles - (cycles % i)

    if i == cycles:
        break

    i += 1

print(data)
ret = load()
print(ret)

assert ret == 94255 or ret == 64
