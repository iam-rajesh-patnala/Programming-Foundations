num1 = int(input())
num2 = int(input())

product = 1

for i in range(num1, num2+1):
    product *= i

print(product)