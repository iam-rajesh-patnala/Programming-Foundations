num = int(input())

for i in range(1, num*2):
    if i == 1 or i == num or i == num*2-1:
        res = num * "* "
        print(res)
    else:
        spaces = "  " * (num-1)
        res = spaces + "*"
        print(res)