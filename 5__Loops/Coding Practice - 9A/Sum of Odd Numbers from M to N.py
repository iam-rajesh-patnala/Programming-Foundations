num1 = int(input())
num2 = int(input())

sum = 0

for i in range(num1, num2 + 1):
    if (i % 2) != 0:
        sum = sum + i
print(sum)
