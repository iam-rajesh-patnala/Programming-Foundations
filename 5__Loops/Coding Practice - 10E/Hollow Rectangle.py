row = int(input())
col = int(input())

for i in range(row):
    if (i == 0) or (i == (row - 1)):
        print("* " * col)
    else:
        numofspaces = "  " * (col - 2)
        print("* " + numofspaces + "* ")
