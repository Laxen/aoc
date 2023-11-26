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
        self.visible = []

    def visible_asteroids(self, data):
        self.visible = []
        for (y, x), val in np.ndenumerate(data):
            if val == "#" and not (self.x == x and self.y == y):
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
                    self.visible.append((y, x))

    def __repr__(self):
        return f"{self.n_visible}"

asteroids = dict()
for (y, x), val in np.ndenumerate(data):
    if val == "#":
        asteroids[(y, x)] = Asteroid(x, y)
        asteroids[(y, x)].visible_asteroids(data)

xbase = 11
ybase = 11

cnt = 0
while True:
    asteroids[(ybase,xbase)].visible_asteroids(data)
    s_vis = sorted(asteroids[(ybase,xbase)].visible, key=lambda item: (np.arctan2(item[0] - ybase, item[1] - xbase) + np.pi / 2) % (2 * np.pi))
    for a in s_vis:
        print(a)
        data[a[0], a[1]] = "."
        cnt += 1
        if cnt == 200:
            print(a[1] * 100 + a[0])
            exit()
