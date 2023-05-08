n = int(input())  # 5

for row in range(1, n + 1):
    i = n - (row - 1)
    left_spaces = " " * (row - 1)
    if (i > 2) and (i < n):
        hollow = "  " * (i - 2)
        numbers = "1 " + hollow + (str(i) + " ")
        print(left_spaces + numbers)

    else:
        numbers = ""
        for j in range(1, i + 1):
            numbers = numbers + (str(j) + " ")
        print(left_spaces + numbers)
        # 1 2 3 4 5
        #  1     4
        #   1   3
        #    1 2
        #     1
