col = int(input())
row = int(input())

spaces = "  "
num = 7

last_digit = num

for i in range(1, col + 1):
    result = ""
    if i == 1 or i == col:
        for j in range(row):
            result += str(num + j) + " "
            last_digit = num + j
        print(result)
    else:
        result = str(num) + " " + ("  " * (row - 2)) + str(last_digit)
        print(result)
