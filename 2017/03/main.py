import sys
import numpy as np
from collections import defaultdict
from pyhelpers import Parser

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    with open(input_file, "r") as f:
        pass

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

map = dict()

def get_ring(idx):
    for ring in range(3, 100000, 2):
        mini = (ring-2)*(ring-2)+1
        maxi = ring*ring
        if idx >= mini and idx <= maxi:
            return ring, idx - mini - (ring - 2) - (ring // 2)

# def get_dist(ring, idx):
#     pos = idx - (ring - 2)**2 - 1



print(get_ring(347991))
# uwu
