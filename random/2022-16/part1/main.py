import sys
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
import re
from pprint import pprint
import time

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

maxi = dfs(start, start, [], 0, 1)
print(maxi)
