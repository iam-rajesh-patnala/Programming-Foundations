n = int(input())    # 5

spaces = n - 1
for i in range(1, n + 1):
    print(" " * spaces, end="")
    if i == n:
        for j in range(1, i + 1):
            print(str(j) + " ", end="")
    else:
        for j in range(1, i + 1):
            if j == 1 or j == i:
                print(str(j) + " ", end="")
            else:
                print("  ", end="")
    spaces = spaces - 1
    print()
    #     1 
    #    1 2 
    #   1   3 
    #  1     4 
    # 1 2 3 4 5 