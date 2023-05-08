N = int(input())

divisible = (N % 5 == 0 and N % 7 == 0) or (N < 7)

if divisible:
    print(N)
else:
    rem_1 = N % 5
    rem_2 = N % 7
    print(rem_1)
    print(rem_2)