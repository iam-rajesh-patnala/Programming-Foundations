M = int(input())
N = int(input())


for i in range(0, M + 2):
    if (i == 0) or (i == M + 1):
        print("+" + ("-" * N) + "+")
    else:
        print("|" + (" " * N) + "|")
