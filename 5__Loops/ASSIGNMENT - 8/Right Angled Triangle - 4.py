num = int(input())


count = 0

while count < 2:
    for i in range(1, num+1):
        result = "* " * i
        print(result)
    count+= 1