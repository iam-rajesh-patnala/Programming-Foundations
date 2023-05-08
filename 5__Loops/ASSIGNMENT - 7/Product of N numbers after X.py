num = int(input())
rep = int(input())

product = 1

for i in range(num+1, num+rep+1):
    product *= i
print(product)