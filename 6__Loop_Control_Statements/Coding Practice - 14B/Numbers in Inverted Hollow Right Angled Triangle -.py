starter = int(input())
col = int(input())


count = 0

for i in range(col):
    result = ""
    left_spaces = "  "
    if i == 0:
        for j in range(col):
            val = starter + j
            result += str(val) + " "
            count = val
        print(result)
    elif i == (col - 1):
        result = left_spaces * (i) + str(count + i)
        print(result)
    else:
        hollow_space = "  "
        result = left_spaces * (i) + str(count + i) + " " + hollow_space * (col - i - 2) + str(count + i + 1)
        count += 1
        print(result)
