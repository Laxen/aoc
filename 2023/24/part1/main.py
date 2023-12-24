import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser, in_bounds
from pprint import pprint
from heapq import heappush, heappop

np.set_printoptions(linewidth=np.inf)
#sys.setrecursionlimit(10000)

def make_data(input_file):
    ret = []
    with open(input_file, "r") as f:
        for line in f:
            l = re.findall(r"(-?\d+)", line)
            ret.append([int(x) for x in l])
    return ret

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
    area_start = 200000000000000
    area_end = 400000000000000
else:
    print("EXAMPLE\n")
    data = make_data("example")
    area_start = 7
    area_end = 27

# -----------------


s = 0
for i, stone1 in enumerate(data):
    for stone2 in data[i+1:]:
        try:
            x = (stone1[1] - stone2[1] + stone2[0] * (stone2[4] / stone2[3]) - stone1[0] * (stone1[4] / stone1[3])) / ((stone2[4] / stone2[3]) - (stone1[4] / stone1[3]))
            y = (stone1[1] + (x - stone1[0]) / stone1[3] * stone1[4])
            t1 = (x - stone1[0]) / stone1[3]
            t2 = (x - stone2[0]) / stone2[3]
        except ZeroDivisionError:
            continue

        if x >= area_start and x <= area_end and y >= area_start and y <= area_end and t1 >= 0 and t2 >= 0:
            # print(stone1)
            # print(stone2)
            # print(x, y, t1, t2)
            s += 1

print(s)
