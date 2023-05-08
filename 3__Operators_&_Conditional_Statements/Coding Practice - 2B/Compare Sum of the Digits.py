N = int(input())
N = str(N)
first_digit = str(N[0])
second_digit = str(N[1])

sum = int(first_digit) + int(second_digit)

if sum > 7:
    print(True)
else:
    print(False)
