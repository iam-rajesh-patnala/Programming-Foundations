num = int(input())


space = " "
star = "* "

for i in range(1, num+1):
    result = space * (num - i) + star * (i) + space * (num*2 - i*2) + star * (i)
    print (result)
