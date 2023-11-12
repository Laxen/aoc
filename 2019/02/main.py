import sys
from pyhelpers import Parser

def make_data(input_file):
    return Parser.ints_to_list(input_file)

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

for i in range(0, len(data), 4):
    print(i)
    code = data[i]
    match code:
        case 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        case 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
        case 99:
            print("EXIT")
            print(data)
            exit()
        case _:
            print("code:", code)
