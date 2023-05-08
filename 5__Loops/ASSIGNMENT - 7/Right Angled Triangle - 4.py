N = int(input())

count = 0
while count < 2:
    for i in range(1, N+1):
        op = "* " * i
        print(op)
    count+= 1
    