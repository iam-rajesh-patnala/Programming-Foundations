num = int(input())

king = num

for i in range(0, num):
    op = i*" " + king*"* "
    king -= 1
    print(op)

queen = num-2

for j in range(2, num+1):
    mp = queen * " " + j * "* "
    queen -= 1
    print(mp)
