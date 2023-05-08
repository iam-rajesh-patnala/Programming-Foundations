num1 = int(input())
num2 = int(input())

count = 0
sum = 0

for i in range(num1, num2+1):
    count += 1
    sum+= i

print(sum, sum/count, sep="\n")