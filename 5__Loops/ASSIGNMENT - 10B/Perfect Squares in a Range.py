num1 = int(input())
num2 = int(input())
count = 0
for i in range(num1, num2 + 1):
    if int(i**0.5) == i**0.5:
        count += 1
print(count)
