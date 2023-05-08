row = int(input())


for i in range(1, row*2):
    result = ""
    if i == 1 or i == row or i == row*2-1:
        for j in range(row):
            result += "* "
        print(result)
    elif i <= row:
        left_space = "  " * (row-1)
        result = left_space + "* "
        print(result)
    else:
        result = "* "
        print(result)
