import sys
import numpy as np
from pyhelpers import Parser
import re
from collections import defaultdict
from datetime import datetime, timedelta

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    with open(input_file, "r") as f:
        data = f.read().splitlines()
    return data

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

data.sort()
sleep = defaultdict(list)
guard = None

for line in data:
    timestamp = re.search(r"\[(.*)\]", line).group(1)
    timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    g = re.search(r" #(.*) begins", line)

    if g is None:
        g = guard
        sleep[guard].append(timestamp)
    else:
        guard = g.group(1)

max_sleep = timedelta(0)
max_guard = 0
maxies = 0
maxies_guard = 0
maxies_min = 0
for g, s in sleep.items():
    sleep_hist = defaultdict(int)
    for i in range(1, len(s), 2):
        start = s[i-1]
        end = s[i]
        delta = timedelta(minutes=1)
        while start < end:
            sleep_hist[start.minute] += 1
            start += delta

    m = max(sleep_hist.items(), key=lambda item: item[1])
    print(m)
    if m[1] > maxies:
        maxies = m[1]
        maxies_guard = g
        maxies_min = m[0]

print(int(maxies_min) * int(maxies_guard))
