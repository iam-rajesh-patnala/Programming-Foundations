num1 = int(input())
num2 = int(input())

numbers_found = False
list_a = []

for i in range(num1, num2+1):
    if i % 9 == 0:
        list_a.append(i)
        numbers_found = True

if numbers_found:
    print(*list_a)
else:
    print("No Numbers found")