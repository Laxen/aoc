import sys
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
import re
import networkx as nx
import matplotlib.pyplot as plt

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    with open(input_file, "r") as f:
        ret = [list(line.strip()) for line in f.readlines()]
    return ret

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

start = []
end = None

G = nx.DiGraph()
for yi, row in enumerate(data):
    for xi, c in enumerate(row):
        if c == "S" or c == "a":
            start.append((xi, yi))
        elif c == "E":
            end = (xi, yi)

        G.add_node((xi, yi), label=c)

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (dx, dy) == (0, 0):
                    continue
                if (dx, dy) == (-1, -1) or (dx, dy) == (-1, 1) or (dx, dy) == (1, -1) or (dx, dy) == (1, 1):
                    continue

                if 0 <= xi + dx < len(data[0]) and 0 <= yi + dy < len(data):
                    nord = ord(data[yi + dy][xi + dx]) if data[yi + dy][xi + dx] != "E" else ord("z")

                    if ord(c) >= nord:
                        G.add_edge((xi, yi), (xi + dx, yi + dy))
                    elif ord(c) == nord - 1:
                        G.add_edge((xi, yi), (xi + dx, yi + dy))
                    elif data[yi][xi] == "S":
                        G.add_edge((xi, yi), (xi + dx, yi + dy))

shortest = 10000000
for s in start:
    try:
        path = nx.shortest_path(G, s, end)
    except nx.NetworkXNoPath:
        continue
    shortest = min(shortest, len(path)-1)
print(shortest)

# pos = {(x,y):(y,-x) for x,y in G.nodes()}
# labels = nx.get_node_attributes(G, "label")
# nx.draw(G, with_labels=True, labels=labels, pos=pos)
# plt.show()
