num = int(input())


for i in range(1, num*2):
    if i == 1 or i == num or i == num*2-1:
        res = "* " * num
        print(res)
    elif i < num:
        res = "* " + "  " * (num-1)
        print(res)
    else:
        res = "  " * (num - 1) + "* "
        print(res)