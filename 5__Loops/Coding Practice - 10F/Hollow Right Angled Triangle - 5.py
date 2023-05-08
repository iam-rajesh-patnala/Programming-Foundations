N = int(input())
m = 1
for i in range(N, 0, -1):
    for j in range(1, i):
        print(" ", end=" ")
    for k in range(1, m + 1):
        if k == 1 or k == m or m == N:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")
    m += 1
