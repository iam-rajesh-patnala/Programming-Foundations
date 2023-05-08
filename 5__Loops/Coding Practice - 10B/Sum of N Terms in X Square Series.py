num1 = int(input())
num2 = int(input())

total = 0

for i in range(1, num2+1):
    val = str(num1) * i
    total += int(val)**2

print(total)

