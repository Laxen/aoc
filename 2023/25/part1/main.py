import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser, in_bounds
from pprint import pprint
from heapq import heappush, heappop
import networkx as nx

np.set_printoptions(linewidth=np.inf)
#sys.setrecursionlimit(10000)

def make_data(input_file):
    g = nx.Graph()

    with open(input_file, "r") as f:
        for line in f:
            line = line.strip().split(": ")
            for con in line[1].split(" "):
                g.add_edge(line[0], con)
    return g

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

edges = nx.minimum_edge_cut(data)
data.remove_edges_from(edges)
s = 1
for con in nx.connected_components(data):
    s *= len(con)
print(s)

# import matplotlib.pyplot as plt
# nx.draw(g, with_labels=True)
# plt.show()
