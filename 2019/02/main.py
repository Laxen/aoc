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

def run(_data):
    for i in range(0, len(_data), 4):
        print(i)
        code = _data[i]
        match code:
            case 1:
                _data[_data[i+3]] = _data[_data[i+1]] + _data[_data[i+2]]
            case 2:
                _data[_data[i+3]] = _data[_data[i+1]] * _data[_data[i+2]]
            case 99:
                if _data[0] == 19690720:
                    print("EXIT")
                    print(100*i1+i2)
                    exit()
                else:
                    return
            case _:
                print("code:", code)
                exit()

for i1 in range(0, 99):
    for i2 in range(0, 99):
        data[1] = i1
        data[2] = i2

        print(data)
        run(data.copy())

