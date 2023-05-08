num = int(input())

for i in range(num):
    if i == 0:
        print("* " * num)
    else:
        print("+ " * (num-i))