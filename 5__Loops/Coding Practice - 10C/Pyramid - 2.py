num = int(input())

space = "  "


for i in range(1, num+1):
    result = space * (num-i) + (str(i)+" ") * (i*2 - 1)
    print(result)