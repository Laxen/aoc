import sys
from pyhelpers import Parser, Coord, Grid
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4).pprint

def make_data(input_file):
    with open(input_file, "r") as f:
        l1 = f.readline().rstrip().split(",")
        l2 = f.readline().rstrip().split(",")
        return l1, l2

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

class HashGrid:
    def __init__(self):
        self.grid = {}

    def find(self, value):
        ret = []
        for key, val in self.grid.items():
            if val == value:
                ret.append(key)
        return ret

    def __repr__(self):
        max_x = max(key[0] for key in self.grid.keys())
        max_y = max(key[1] for key in self.grid.keys())
        min_x = min(key[0] for key in self.grid.keys())
        min_y = min(key[1] for key in self.grid.keys())

        array = [[0] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
        for key, value in self.grid.items():
            array[key[1] - min_y][key[0] - min_x] = value

        return "\n".join("".join(str(x) for x in row) for row in array)

    def __contains__(self, key):
        return key in self.grid

    def __getitem__(self, key):
        if key not in self.grid:
            return None
        return self.grid[key]

    def __setitem__(self, key, value):
        self.grid[key] = value

l1 = data[0]
l2 = data[1]

x = 0
y = 0
steps = 0

grid = HashGrid()
stepgrid = HashGrid()

for c in l1:
    n = int(c[1:])
    match c[0]:
        case "R":
            for i in range(n):
                x += 1
                steps += 1
                grid[(x, y)] = 1
                stepgrid[(x, y)] = steps
        case "L":
            for i in range(n):
                x -= 1
                steps += 1
                grid[(x, y)] = 1
                stepgrid[(x, y)] = steps
        case "U":
            for i in range(n):
                y -= 1
                steps += 1
                grid[(x, y)] = 1
                stepgrid[(x, y)] = steps
        case "D":
            for i in range(n):
                y += 1
                steps += 1
                grid[(x, y)] = 1
                stepgrid[(x, y)] = steps

x = 0
y = 0
steps = 0

intersection_steps = []

for c in l2:
    n = int(c[1:])
    match c[0]:
        case "R":
            for i in range(n):
                x += 1
                steps += 1
                if grid[(x, y)] == 1:
                    grid[(x, y)] = 3
                    intersection_steps.append(stepgrid[(x, y)] + steps)
                else:
                    grid[(x, y)] = 2
        case "L":
            for i in range(n):
                x -= 1
                steps += 1
                if grid[(x, y)] == 1:
                    grid[(x, y)] = 3
                    intersection_steps.append(stepgrid[(x, y)] + steps)
                else:
                    grid[(x, y)] = 2
        case "U":
            for i in range(n):
                y -= 1
                steps += 1
                if grid[(x, y)] == 1:
                    grid[(x, y)] = 3
                    intersection_steps.append(stepgrid[(x, y)] + steps)
                else:
                    grid[(x, y)] = 2
        case "D":
            for i in range(n):
                y += 1
                steps += 1
                if grid[(x, y)] == 1:
                    grid[(x, y)] = 3
                    intersection_steps.append(stepgrid[(x, y)] + steps)
                else:
                    grid[(x, y)] = 2

# intersections = grid.find(3)
# intersections = [abs(x) + abs(y) for x, y in intersections]

#print(grid)
# pp(min(intersections))

pp(min(intersection_steps))
