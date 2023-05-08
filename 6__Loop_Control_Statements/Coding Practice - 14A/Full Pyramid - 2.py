n = int(input())    # 5

for i in range(1, n + 1):
    left_spaces = " " * (n - i)
    numbers = ""
    for j in range(1, i + 1):
        numbers = numbers + (str(j) + " ")
    print(left_spaces + numbers)
    #     1 
    #    1 2 
    #   1 2 3 
    #  1 2 3 4 
    # 1 2 3 4 5 