num = int(input())

space = "  "
star = "* "

for i in range(1, num+1):
    result = space * (num-i) + star * (i*2-1)
    print(result)