num = int(input())

star = "* "

for i in range(1, num+1):
    left_space = "  " * (num -i)
    result = left_space + star * i
    print(result)