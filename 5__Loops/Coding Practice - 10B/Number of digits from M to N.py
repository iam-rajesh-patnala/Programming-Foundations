num1 = int(input())
num2 = int(input())

single = 0
double = 0
triple = 0

for num in range(num1, num2+1):
    if num <= 9:
        single += 1
    elif num <= 99:
        double += 2
    else:
        triple+= 3

total = single + double

print(total)