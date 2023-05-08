num = int(input())

result = []

for i in range(1, num+1):
    if i % 3 == 0 and i % 2 == 0:
        result.append(i)

print(len(result))