N = int(input())
for line_number in range(1, N + 1):
    if line_number > 1 and line_number < N:
        print("* " * line_number)
    else:
        print("* " + "  " * (line_number - 2) + "* ")
