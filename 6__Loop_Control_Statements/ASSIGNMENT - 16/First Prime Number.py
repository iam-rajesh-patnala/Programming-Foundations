a = int(input())

for i in range(a):
    b = int(input())
    count = 0
    for j in range(2, b+1):
        if (b % j) == 0:
            count += 1
    if count == 1:
        print(b)
        break
