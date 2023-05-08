num1 = int(input())
num2 = int(input())

total = 0

for i in range(1, (num2) * 2 + 1):
    if i % 2 != 0:
        val = num1**i
        total += val
        
print(total)