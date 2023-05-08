num = int(input())  # 5

total = 0
for i in range(1, num + 1):
    total += 1 / i
print(round(total, 2))  # 2.28
