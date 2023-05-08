num = int(input())

count = 0
for i in range(1, num+1):
    num2 = int(input())
    for j in range(1):
        count = count + num2
        avg = count/i
    print(round(avg, 3))