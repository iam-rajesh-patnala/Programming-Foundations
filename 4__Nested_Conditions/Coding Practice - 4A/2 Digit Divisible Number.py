N = int(input())

str_N = str(N)

first_digit = int(str_N[0])
second_digit = int(str_N[1])


if (N % first_digit == 0 and N % second_digit == 0):
    print(N * 2)
else:
    print(N)