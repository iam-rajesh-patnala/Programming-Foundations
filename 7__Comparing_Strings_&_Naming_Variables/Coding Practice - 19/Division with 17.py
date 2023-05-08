num = int(input())


result = []

for i in range(num):
    num2 = int(input())
    val = num2 // 17
    result.append(val)

print(*result, sep="\n")