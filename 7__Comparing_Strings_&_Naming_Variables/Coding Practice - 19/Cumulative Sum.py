num = int(input())


total = []
sum = 0

for i in range(num):
    num2 = int(input())
    sum += num2
    total.append(sum)

print(*total, sep="\n")
