num1 = int(input())
num2 = int(input())


val = []

for i in range(num1, num2+1):
    if i % 2 != 0:
        val.append(i)

for j in range(1, len(val)+1):
    print(val[-j], end=" ")
