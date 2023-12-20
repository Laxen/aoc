import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
from pprint import pprint
from ordered_set import OrderedSet

np.set_printoptions(linewidth=np.inf)

class Module:
    def __init__(self, name, type, connections):
        self.name = name
        self.type = type
        self.connections = connections

        # &
        self.inputs = dict()

        # %
        self.output = False

    def receive_input(self, name, pulse):
        if self.type == "&":
            self.inputs[name] = pulse

            if all(self.inputs.values()):
                return 0
            return 1

        if self.type == "%":
            if pulse == 0:
                self.output = not self.output
                return int(self.output)
            return None

        # raise Exception("Unknown type", self.name, self.type)

    def __repr__(self):
        if self.type == "&":
            return f"{self.name} {self.type} {self.connections} {self.inputs}"
        return f"{self.name} {self.type} {self.connections}"

def make_data(input_file):
    ret = defaultdict(lambda: Module("", "", []))
    with open(input_file, "r") as f:
        for line in f:
            sp = line.strip().split(" -> ")
            if sp[0][0] == "%" or sp[0][0] == "&":
                m = Module(sp[0][1:], sp[0][0], sp[1].split(", "))
                ret[m.name] = m
            else:
                m = Module(sp[0], " ", sp[1].split(", "))
                ret[m.name] = m
    return ret

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

def init_modules():
    for module in data.values():
        if module.type == "&":
            for m in data.values():
                if m.name == module.name:
                    continue

                if module.name in m.connections:
                    module.inputs[m.name] = 0

init_modules()
pending_modules = []

low_count = 0
high_count = 0

stamps = defaultdict(lambda: 0)
cycles = defaultdict(lambda: 0)

for i in range(100000):
    pending_modules.append(("broadcaster", 0))
    low_count += 1

    while pending_modules:
        new_pending_modules = []

        for module, pulse in pending_modules:
            module = data[module]

            if module.name in ["lk", "zv", "sp", "xt"]:
                if pulse == 1:
                    print(module.name, i - stamps[module.name])
                    cycles[module.name] = i - stamps[module.name]
                    stamps[module.name] = i

            for m in module.connections:
                m = data[m]

                output = m.receive_input(module.name, pulse)
                # print(module.type, module.name, pulse, ">", m.name)

                if output is not None:
                    new_pending_modules.append((m.name, output))

                if pulse == 1:
                    high_count += 1
                elif pulse == 0:
                    low_count += 1

        pending_modules = new_pending_modules
        # print("---", low_count, high_count, "---")
    # print("-------------------------")

s = 1
for cycle in cycles.values():
    print(cycle)
    s *= cycle
print(s)
