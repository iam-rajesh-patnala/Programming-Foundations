num = int(input())

count = 0

while count < 2:
    for i in range(1, num+1):
        print(str(i) * i)
    count+= 1