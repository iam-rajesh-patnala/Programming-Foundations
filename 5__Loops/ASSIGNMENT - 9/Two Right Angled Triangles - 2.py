num = int(input())

for i in range(1, num+1):
    print("* " * i)

for j in range(num):
    print("* " * (num-j))