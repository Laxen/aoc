import sys
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser, intersect
import re, time

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    ret = []
    seeds = []
    with open(input_file, "r") as f:
        for line in f:
            if line.startswith("seeds"):
                seeds = [int(i) for i in re.findall(r'\d+', line)]
            elif line == "\n":
                ret.append([])
            elif ":" not in line:
                ret[-1].append([int(i) for i in re.findall(r'\d+', line)])
    return seeds, ret

if len(sys.argv) > 1:
    print("INPUT\n")
    seeds, data = make_data("input")
else:
    print("EXAMPLE\n")
    seeds, data = make_data("example")

# -----------------

def map_source_dest(interval, map_line):
    dest_start = map_line[0]
    source_start = map_line[1]
    range_len = map_line[2]
    if interval[0] >= source_start and interval[1] <= source_start + range_len:
        return (dest_start + interval[0] - source_start, dest_start + interval[1] - source_start)
    raise Exception(f"{interval} not in {map_line}")

seed_intervals = []
for i in range(1, len(seeds), 2):
    seed_intervals.append((seeds[i-1], seeds[i-1] + seeds[i]))

new_seed_intervals = set()

for map in data:
    for mapline in map:
        seed_i = 0
        while seed_i < len(seed_intervals):
            seed_interval = seed_intervals[seed_i]
            dest_interval = (mapline[1], mapline[1] + mapline[2])
            overlap, nonintersects = intersect([seed_interval], [dest_interval])
            if overlap:
                overlap = overlap[0]
                if overlap not in new_seed_intervals:
                    new_seed_intervals.add(map_source_dest(overlap, mapline))
                else:
                    seed_i += 1
                    continue

                del seed_intervals[seed_i]
                for nonintersect in nonintersects:
                    seed_intervals += nonintersect
                seed_i = 0
            else:
                seed_i += 1

    for seed in new_seed_intervals:
        if seed not in seed_intervals:
            seed_intervals.append(seed)
    new_seed_intervals = set()

seed_intervals = sorted(seed_intervals, key=lambda item: item[0])
s = seed_intervals[0][0]

print(s)
