import sys
import numpy as np
from pyhelpers import Parser

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
        return np.array([list(line.strip()) for line in lines])

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n_visible = 0

    def visible_asteroids(self, data):
        print("starting for", self.y, self.x)
        for (y, x), val in np.ndenumerate(data):
            if val == "#" and not (self.x == x and self.y == y):
                print("  found", y, x)
                dx = x - self.x
                dy = y - self.y
                gcd = np.gcd(dx, dy)
                dx = dx // gcd
                dy = dy // gcd

                tx = self.x + dx
                ty = self.y + dy
                while not (tx == x and ty == y):
                    if data[ty, tx] == "#":
                        break

                    tx += dx
                    ty += dy
                else:
                    self.n_visible += 1

    def __repr__(self):
        return f"{self.n_visible}"

asteroids = dict()
for (y, x), val in np.ndenumerate(data):
    if val == "#":
        asteroids[(y, x)] = Asteroid(x, y)
        asteroids[(y, x)].visible_asteroids(data)

print(dict(sorted(asteroids.items(), key=lambda item: item[1].n_visible, reverse=True)))
