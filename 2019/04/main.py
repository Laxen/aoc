import sys
from pyhelpers import Parser

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

def is_valid(num):
    counter = {}
    for i in range(len(num)):
        if num[i] not in counter:
            counter[num[i]] = 1
        else:
            counter[num[i]] += 1
        if i > 0 and num[i] < num[i - 1]:
            return False
    return 2 in counter.values()

count = 0
for i in range(246515, 739105 + 1):
    if is_valid(str(i)):
        count += 1
print(count)
