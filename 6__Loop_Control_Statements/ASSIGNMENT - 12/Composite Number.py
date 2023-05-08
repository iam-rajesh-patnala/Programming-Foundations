N = int(input())

fact = 0

for i in range(2, N):
    if (N % i) == 0:
        fact = fact + 1

if fact > 1:
    print("True")
else:
    print("False")
