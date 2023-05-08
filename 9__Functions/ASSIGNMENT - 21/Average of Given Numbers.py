num = input().split()

length = len(num)
total = 0

for i in num:
    total += int(i)

print(round(total / length, 2))
