num = int(input())


for i in range(1, num + 1):
    result = ""
    left_spaces = "  " * (num - i)
    for j in range(i):
        result += str(i - j) + " "
    print(left_spaces + result)
