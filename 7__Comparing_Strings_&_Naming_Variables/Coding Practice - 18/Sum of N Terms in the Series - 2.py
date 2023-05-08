num = float(input())
num2 = int(input())

total = 0

for i in range(1, num2 + 1):
    val = num**i
    total += val

print(round(total, 4))
