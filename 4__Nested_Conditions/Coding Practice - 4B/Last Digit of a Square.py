N = int(input())

Square = str(N**2)
N = str(N)

Square_last_digit, input_last_digit  = (int(Square[-1]), int(N[-1]))

if Square_last_digit == input_last_digit:
    print("Equal")
else:
    print("Not equal")


