n = int(input())

for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if (i == 1 and j % 2 != 0) or i == j or i + j == n * 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
