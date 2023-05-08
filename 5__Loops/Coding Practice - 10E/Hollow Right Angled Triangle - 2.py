n = int(input())
n1 = n + 1
print("_" * n1)
for i in range(1, n1):
    print("|" + " " * (n - i) + "/")
    # TODO: write code...
