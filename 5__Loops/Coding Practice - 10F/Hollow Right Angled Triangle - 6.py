N = int(input())
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j == N or i == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
