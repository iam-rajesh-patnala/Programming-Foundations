num1 = int(input())
num2 = int(input())

total = 0
for i in range(num1, num2 + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            total += i

print(total)