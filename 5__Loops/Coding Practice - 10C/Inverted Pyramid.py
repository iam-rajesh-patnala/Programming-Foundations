num = int(input())

space = " "
star = "*"

for i in range(1, num + 1):
    result = space * (i - 1) + star * (num * 2 - (i * 2 - 1))
    print(result)
