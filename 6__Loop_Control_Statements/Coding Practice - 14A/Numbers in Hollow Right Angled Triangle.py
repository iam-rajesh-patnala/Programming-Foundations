n = int(input())  # 5


for i in range(1, n + 1):
    if (i > 2) and (i < n):
        hollow_spaces = "  " * (i - 2)
        numbers = "1 " + hollow_spaces + (str(i) + " ")
        print(numbers)
    else:
        numbers = ""
        for j in range(1, i + 1):
            numbers = numbers + (str(j) + " ")
        print(numbers)
        # 1
        # 1 2
        # 1   3
        # 1     4
        # 1 2 3 4 5
