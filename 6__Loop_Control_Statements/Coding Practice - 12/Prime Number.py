number = int(input())

fact = 0

for i in range(2, number):
    if number % i == 0:
        fact = fact + 1
if fact == 0:
    print("Prime Number")
else:
    print("Not a Prime Number")
