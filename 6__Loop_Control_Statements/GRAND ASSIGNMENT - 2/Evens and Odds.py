num1 = int(input())
num2 = int(input())


odd_count = 0
even_count = 0

for i in range(num1, num2+1):
    if i % 2 == 0:
        even_count += 1
    elif i % 2 == 1:
        odd_count += 1
print(odd_count)
print(even_count)
