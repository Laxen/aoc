import sys
from pyhelpers import Parser

def make_data(input_file):
    return Parser.row_to_int(input_file)

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

def mass_to_fuel(mass):
    return int(mass / 3) - 2

print(sum([mass_to_fuel(mass) for mass in data]))
