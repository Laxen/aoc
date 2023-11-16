import sys
from pyhelpers import Parser

def make_data(input_file):
    with open(input_file, "r") as f:
        return f.read().rstrip().split(",")

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

def handle_instr(instr):
    global pc, data

    instr = instr.zfill(5)
    opcode = instr[-2:]

    if opcode == "01":
        print("ADD")
        mode1 = instr[-3:-2]
        mode2 = instr[-4:-3]

        if mode1 == "0":
            d1 = data[int(data[pc+1])]
        elif mode1 == "1":
            d1 = data[pc+1]

        if mode2 == "0":
            d2 = data[int(data[pc+2])]
        elif mode2 == "1":
            d2 = data[pc+2]

        print(f"{d1} + {d2} -> {int(data[pc+3])}")

        data[int(data[pc+3])] = str(int(d1) + int(d2))

        pc += 4
    elif opcode == "02":
        mode1 = instr[-3:-2]
        mode2 = instr[-4:-3]

        if mode1 == "0":
            d1 = data[int(data[pc+1])]
        elif mode1 == "1":
            d1 = data[pc+1]

        if mode2 == "0":
            d2 = data[int(data[pc+2])]
        elif mode2 == "1":
            d2 = data[pc+2]

        print(f"{d1} * {d2} -> {int(data[pc+3])}")

        data[int(data[pc+3])] = str(int(d1) * int(d2))

        pc += 4
    elif opcode == "03":
        i = input("IN: ")
        data[int(data[pc+1])] = i
        pc += 2
    elif opcode == "04":
        mode = instr[-3:-2]
        if mode == "0":
            d = data[int(data[pc+1])]
        elif mode == "1":
            d = data[pc+1]
        print("OUT: ", d)
        pc += 2
    elif opcode == "05":
        mode1 = instr[-3:-2]
        mode2 = instr[-4:-3]

        if mode1 == "0":
            d1 = data[int(data[pc+1])]
        elif mode1 == "1":
            d1 = data[pc+1]

        if mode2 == "0":
            d2 = data[int(data[pc+2])]
        elif mode2 == "1":
            d2 = data[pc+2]

        if int(d1) != 0:
            pc = int(d2)
        else:
            pc += 3
    elif opcode == "06":
        mode1 = instr[-3:-2]
        mode2 = instr[-4:-3]

        if mode1 == "0":
            d1 = data[int(data[pc+1])]
        elif mode1 == "1":
            d1 = data[pc+1]

        if mode2 == "0":
            d2 = data[int(data[pc+2])]
        elif mode2 == "1":
            d2 = data[pc+2]

        if int(d1) == 0:
            pc = int(d2)
        else:
            pc += 3
    elif opcode == "07":
        mode1 = instr[-3:-2]
        mode2 = instr[-4:-3]

        if mode1 == "0":
            d1 = data[int(data[pc+1])]
        elif mode1 == "1":
            d1 = data[pc+1]

        if mode2 == "0":
            d2 = data[int(data[pc+2])]
        elif mode2 == "1":
            d2 = data[pc+2]

        if int(d1) < int(d2):
            data[int(data[pc+3])] = 1
        else:
            data[int(data[pc+3])] = 0

        pc += 4
    elif opcode == "08":
        mode1 = instr[-3:-2]
        mode2 = instr[-4:-3]

        if mode1 == "0":
            d1 = data[int(data[pc+1])]
        elif mode1 == "1":
            d1 = data[pc+1]

        if mode2 == "0":
            d2 = data[int(data[pc+2])]
        elif mode2 == "1":
            d2 = data[pc+2]

        if int(d1) == int(d2):
            data[int(data[pc+3])] = 1
        else:
            data[int(data[pc+3])] = 0

        pc += 4
    elif opcode == "99":
        print("HALT")
        print(data)
        sys.exit(0)

pc = 0

while pc < len(data):
    print("PC", pc)
    instr = data[pc]
    handle_instr(instr)
