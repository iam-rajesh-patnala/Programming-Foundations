num = int(input())

number = 1

for i in range(1, num + 1):
    exp = ""
    for j in range(i):
        exp = exp + str(number) + " "
        number = int(number) + 1
    print(exp)








m = int(input())
n = int(input())