num_1 = int(input())
num_2 = int(input())

less = num_1 < 20 or num_2 < 20
grater = num_1 > 30 or num_2 > 30

if less and grater:
    print(True)
else:
    print(False)
