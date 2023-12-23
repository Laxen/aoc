with open("hikes", "r") as f:
    num = 0
    for line in f:
        num = max(num, int(line.strip().split(" ")[-1]))
    print(num)

# Not 5902
# Not 5930
# Not 6058, too low
# Not 6070
