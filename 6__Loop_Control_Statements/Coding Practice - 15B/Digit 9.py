num = int(input())  # 4

star = "* "
space = "  "
for i in range(1, num + 1):
    if i == 1 or i == num:
        print(star * num)
    else:
        print(star + space * (num - 2) + star)
for j in range(1, num):
    if j == num - 1:
        print(star * num)
    else:
        print(space * (num - 1) + star)
        # * * * *
        # *     *
        # *     *
        # * * * *
        #       *
        #       *
        # * * * *
