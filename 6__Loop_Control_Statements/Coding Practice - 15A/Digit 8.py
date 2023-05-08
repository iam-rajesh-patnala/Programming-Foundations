num = int(input())  # 5

for i in range(0, (num * 2) + 1):
    if i == 0 or i == num or i == (num * 2):
        print("* " * num)
    else:
        print("* " + ("  " * (num - 2)) + "* ")
        #   * * * * *
        #   *       *
        #   *       *
        #   *       *
        #   *       *
        #   * * * * *
        #   *       *
        #   *       *
        #   *       *
        #   *       *
        #   * * * * *
