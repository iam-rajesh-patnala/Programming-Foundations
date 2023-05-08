N = int(input())

divisibility = (N % 2) and (N % 3) and (N % 5) and (N % 7) != 0

if divisibility:
    print("True")
else:
    print("False")
    # TODO: write code...
