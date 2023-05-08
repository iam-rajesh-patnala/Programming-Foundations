num = int(input())


spaces = "  "
star = "* "

for i in range(1, num + 1):
    res = star * i + spaces * (num*2 - (i*2)) + star * i
    print(res)  
