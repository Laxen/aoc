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
for g, s in sleep.items():
    sleep_time = timedelta(0)
    for i in range(1, len(s), 2):
        sleep_time += s[i] - s[i-1]
        # print("guard", g, ":", s[i-1], "-", s[i], "tot", sleep_time)

    if sleep_time > max_sleep:
        max_sleep = sleep_time
        max_guard = g

s = sleep[max_guard]
sleep_max = defaultdict(int)
for i in range(1, len(s), 2):
    start = s[i-1]
    end = s[i]
    delta = timedelta(minutes=1)
    while start < end:
        sleep_max[start.minute] += 1
        start += delta

# sleep_max = dict(sorted(sleep_max.items(), key=lambda item: item[1], reverse=True))
# print(sleep_max[0])
m = max(sleep_max.items(), key=lambda item: item[1])[0]
print(int(m) * int(max_guard))
