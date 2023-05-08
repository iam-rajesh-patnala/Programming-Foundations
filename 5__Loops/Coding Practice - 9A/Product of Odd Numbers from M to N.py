num1 = int(input())
num2 = int(input())

total = 1

for i in range(num1, num2+1):
    if i % 2 != 0:
        total*= i

print(total)