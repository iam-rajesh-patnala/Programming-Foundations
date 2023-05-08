M = int(input())
N = int(input())


for i in range(M):
    if (i % 2) == 0:
        print("+ " * N)
    else:
        print("- " * N)
