A = int(input())

B = int(input())

condition_1 = A % 3 == 0 and B % 3 == 0
condition_2 = A % 12 == 0 or B % 12 == 0

if condition_1 and condition_2:
    print('Pair')
else:
    print("Not a pair")