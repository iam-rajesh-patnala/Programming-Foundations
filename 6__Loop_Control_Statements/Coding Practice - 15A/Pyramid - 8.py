row = int(input())

starter = 2

for i in range(1, row + 1):
    spaces = "  " * (row - i)
    res = spaces + "* " * starter
    starter += 2
    print(res)
