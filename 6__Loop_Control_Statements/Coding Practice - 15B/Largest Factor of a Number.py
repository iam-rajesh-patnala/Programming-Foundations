num = int(input())

factors = []

for i in range(1, num+1):
    if num % i == 0:
        factors.append(i)

print(factors[-2])