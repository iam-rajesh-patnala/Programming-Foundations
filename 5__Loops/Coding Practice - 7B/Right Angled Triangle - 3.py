num = int(input())

for i in range(1, num+1):
    if i <= num-1:
        print("* " * i)
    else:
        print("+ " * i)