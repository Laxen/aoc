import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser, overlaps
from pprint import pprint
from copy import deepcopy

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    ret = []
    with open(input_file, "r") as f:
        for line in f:
            r1, r2 = line.strip().split("~")
            r1 = r1.split(",")
            r2 = r2.split(",")
            r1 = [int(r1[0]), int(r1[1]), int(r1[2])]
            r2 = [int(r2[0]), int(r2[1]), int(r2[2])]
            rx = [r1[0], r2[0]]
            ry = [r1[1], r2[1]]
            rz = [r1[2], r2[2]]
            ret.append([rx, ry, rz])
    return ret

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

def settle():
    new_data = []
    supported_by = []

    for r in data:
        new_r = deepcopy(r)

        supported_by.append([])
        overlap = False

        while not overlap:
            if new_r[2][0] > 1:
                new_r[2][0] -= 1
                new_r[2][1] -= 1
            else:
                break

            for i, r_ in enumerate(data):
                if r_ == r:
                    continue

                if overlaps(new_r, r_):
                    # print("overlap", new_r, r_)
                    overlap = True
                    supported_by[-1].append(i)

        if overlap:
            new_r[2][0] += 1
            new_r[2][1] += 1
            new_data.append(new_r)
        else:
            new_data.append(new_r)

    return new_data, supported_by

new_data = []
supported_by = []
while new_data != data:
    data = new_data if new_data else data
    new_data, supported_by = settle()

print("Settle done")
pprint(data)
pprint(supported_by)

supports = defaultdict(lambda: True)
for l in supported_by:
    if len(l) == 1:
        supports[l[0]] = False

print("Supports done")

orig_supported_by = deepcopy(supported_by)
s = 0
for dis in range(len(data)):
    removes = [dis]
    supported_by = deepcopy(orig_supported_by)

    i = 0
    while True:
        if i == len(data):
            break

        for remove in removes:
            if remove in supported_by[i]:
                supported_by[i].remove(remove)
                if len(supported_by[i]) == 0:
                    removes.append(i)
                    i = 0
                    s += 1
                    break
        else:
            i += 1

print(s)
