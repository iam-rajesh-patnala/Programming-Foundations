num = int(input())  # 4


count = 1

for i in range(num * 2):
    if i == 0 or i == num * 2 - 1:
        print("|")
    elif i < num:
        space = " " * i
        val = "|" + space + "\\"
        print(val)
    else:
        space = " " * (num - count)
        count += 1
        val = "|" + space + "/"
        print(val)

        # |
        # | \
        # |  \
        # |   \
        # |   /
        # |  /
        # | /
        # |
