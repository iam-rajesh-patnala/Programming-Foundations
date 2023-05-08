num = int(input())

space = " "
star = "* "
for i in range(0, num):
    add = space * i + star * num
    num = num - 1
    print(add)
