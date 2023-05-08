num1 = int(input())
num2 = int(input())

total = 0
for i in range(num1, num2 + 1):
    total += i**2

print(total)
