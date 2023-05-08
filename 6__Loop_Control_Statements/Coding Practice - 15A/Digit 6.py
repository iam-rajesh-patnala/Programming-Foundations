num = int(input())  # 4

star = "* "
space = "  "
for i in range(1, num * 2):
    if i == 1 or i == num * 2 - 1 or i == num:
        result = star * num
        print(result)
    elif i > num:
        result = star + (space * (num - 2)) + star
        print(result)
    else:
        result = star
        print(result)
        #   * * * *
        #   *
        #   *
        #   * * * *
        #   *     *
        #   *     *
        #   * * * *
