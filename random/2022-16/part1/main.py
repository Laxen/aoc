import sys
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
import re
from pprint import pprint
import time
import networkx as nx
import matplotlib.pyplot as plt

np.set_printoptions(linewidth=np.inf)

class Valve:
    def __init__(self, name, flow_rate, tunnels):
        self.name = name
        self.flow_rate = flow_rate
        self.tunnels = tunnels

    def __repr__(self):
        return f"Valve(name={self.name}, flow_rate={self.flow_rate}, tunnels={self.tunnels})"

def make_data(input_file):
    ret = dict()
    with open(input_file, "r") as f:
        for line in f:
            m = re.search(r"Valve (.*) has flow rate=(\d+); tunnel[s]? lead[s]? to valve[s]? (.*)", line)
            valve = m.group(1)
            flow_rate = int(m.group(2))
            tunnels = m.group(3).split(", ")
            ret[valve] = Valve(valve, flow_rate, tunnels)
    return ret

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

start = data["AA"]

cache = defaultdict(lambda:0)

def make_graph(data):
    G = nx.Graph()
    for valve in data.values():
        for tunnel in valve.tunnels:
            G.add_node(valve.name, flow_rate=valve.flow_rate)
            G.add_node(tunnel, flow_rate=data[tunnel].flow_rate)
            G.add_edge(valve.name, tunnel)

    simplified = nx.Graph()
    valves = [valve for valve in data.values() if valve.flow_rate > 0]
    valves.append(start)
    for v1 in valves:
        for v2 in valves:
            if v1.name != v2.name:
                if nx.has_path(G, v1.name, v2.name):
                    simplified.add_node(v1.name, flow_rate=v1.flow_rate)
                    simplified.add_node(v2.name, flow_rate=v2.flow_rate)
                    simplified.add_edge(v1.name, v2.name, weight=nx.shortest_path_length(G, v1.name, v2.name))

    return simplified

def dfs(valve, prev_valve, opened_valves, total_flow, step):
    # print(valve.name, opened_valves, total_flow, step)
    # time.sleep(0.1)

    max_flow = 0
    total_flow += sum([data[v].flow_rate for v in opened_valves])

    if step == 30:
        return total_flow

    if cache[(valve.name, tuple(opened_valves), step)] > total_flow:
        return 0
    else:
        cache[(valve.name, tuple(opened_valves), step)] = total_flow

    if valve.flow_rate > 0 and valve.name not in opened_valves:
        max_flow = dfs(valve, valve, opened_valves + [valve.name], total_flow, step + 1)

    for n in valve.tunnels:
        nvalve = data[n]
        if nvalve.name != prev_valve.name:
            max_flow = max(max_flow, dfs(nvalve, valve, opened_valves, total_flow, step + 1))

    return max_flow

def nx_dfs(valve, prev_valve, opened_valves, total_flow, step):
    if step >= 30:
        return 0

    max_flow = 0
    # This depends on when the valve was opened now, need to keep track of that?
    total_flow += sum([G.nodes[v]["flow_rate"] for v in opened_valves])

    if G.nodes[valve]["flow_rate"] > 0 and valve not in opened_valves:
        max_flow = nx_dfs(valve, valve, opened_valves + [valve], total_flow + sum([G.nodes[v]["flow_rate"] for v in opened_valves]), step + 1)

    for nvalve in nx.neighbors(G, valve):
        if nvalve != prev_valve:
            steps = G.edges[valve, nvalve]["weight"]
            max_flow = max(max_flow, nx_dfs(nvalve, valve, opened_valves, total_flow + sum([G.nodes[v]["flow_rate"] for v in opened_valves])*steps, step + steps))
    return max_flow

# maxi = dfs(start, start, [], 0, 1)
# print(maxi)
G = make_graph(data)
print(nx_dfs("AA", "AA", [], 0, 1))

# Draw
# labels = nx.get_edge_attributes(G,'weight')
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True)
# nx.draw_networkx_edge_labels(G, pos, font_weight='bold', edge_labels=labels)
# plt.show()
