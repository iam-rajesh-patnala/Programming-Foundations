num = int(input())
power = int(input())

sum = 0

for i in range(1, num + 1):
    powers = i**power
    sum = sum + powers
print(sum)
