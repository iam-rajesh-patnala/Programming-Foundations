n = int(input())  # 5
for i in range(1, n):
    spacess = " " * (n - i)
    pattern = ""
    for k in range(1, i + 1):
        pattern += str(k) + " "
    print(spacess + pattern)
for row in range(1, n + 1):
    i = n - (row - 1)
    spacess = " " * (n - i)
    pattern = ""
    for k in range(1, i + 1):
        pattern += str(k) + " "
    print(spacess + pattern)
    #     1
    #    1 2
    #   1 2 3
    #  1 2 3 4
    # 1 2 3 4 5
    #  1 2 3 4
    #   1 2 3
    #    1 2
    #     1
