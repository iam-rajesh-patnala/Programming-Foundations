num1 = int(input())
num2 = int(input())

count = []

for i in range(1, num1+1):
    if i % num2 == 0:
        count.append(i)

print(len(count))
