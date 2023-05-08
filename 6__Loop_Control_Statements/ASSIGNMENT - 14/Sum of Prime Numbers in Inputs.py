num = int(input())

sum = 0

for i in range(num):
    number = int(input())
    if number > 1:
        factors = 0
        for j in range(2, number):
            if number % j == 0:
                factors += 1
        if factors == 0:
            sum += number

print(sum)
