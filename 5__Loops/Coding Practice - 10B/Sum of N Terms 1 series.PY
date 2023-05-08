num = int(input())

sum = 0

for i in range(1, num + 1):
    digit = "1" * i
    sum = sum + int(digit)
print(sum)
