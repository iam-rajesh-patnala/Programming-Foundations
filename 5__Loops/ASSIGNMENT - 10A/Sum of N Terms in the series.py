num1 = int(input())
num2 = int(input())

sum = 0
val = 1

for i in range(num2):
    sum += val * (num1 ** (2 * i + 1))
    val *= -1
print(sum)
