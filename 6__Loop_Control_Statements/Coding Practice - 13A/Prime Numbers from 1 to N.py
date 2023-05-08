num = int(input())

for number in range(2, num + 1):
    fact = 0
    for i in range(2, number):
        if (number % i) == 0:
            fact = fact + 1
    if fact == 0:
        print(number)
