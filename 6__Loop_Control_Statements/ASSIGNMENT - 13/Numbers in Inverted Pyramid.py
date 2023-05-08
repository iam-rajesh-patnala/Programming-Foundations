num = int(input())  # 5


for i in range(0, num):
    space = " "
    space = space * i
    number = ""
    for j in range(1, num + 1):
        number = number + str(j) + " "
    num = num - 1
    print(space + number)

    # 1 2 3 4 5
    #  1 2 3 4
    #   1 2 3
    #    1 2
    #     1
