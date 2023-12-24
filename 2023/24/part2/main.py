import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser, in_bounds
from pprint import pprint
from heapq import heappush, heappop
import z3

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

x = z3.Int('x')
y = z3.Int('y')
z = z3.Int('z')
vx = z3.Int('vx')
vy = z3.Int('vy')
vz = z3.Int('vz')

s = z3.Solver()

for i, (px, py, pz, pvx, pvy, pvz) in enumerate(data[:4]):
    t = z3.Int(f't{i}')
    s.add(t >= 0)
    s.add(x + vx*t == px + pvx*t)
    s.add(y + vy*t == py + pvy*t)
    s.add(z + vz*t == pz + pvz*t)

s.check()
m = s.model()
x, y, z = m.eval(x), m.eval(y), m.eval(z)
x, y, z = int(str(x)), int(str(y)), int(str(z))
print(x + y + z)
