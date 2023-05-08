num = int(input())
res = ""
king = ""

for i in range(1, num+1):
    res = res + str(i)
    for k in range(1):
        fin = res + king
        king = str(i) + king
        print(fin)
