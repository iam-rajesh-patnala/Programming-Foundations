n = int(input())
for i in range(n):
    print((" ".join(["*"] * (i + 1))).rjust(2 * n - 1))
