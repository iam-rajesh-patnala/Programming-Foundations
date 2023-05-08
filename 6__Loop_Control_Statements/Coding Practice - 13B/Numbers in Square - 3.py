num = int(input())

number = 1

for i in range(num):
    add = ""
    for j in range(num):
        add = add + str(number) + " "
        number = number + 1
    print(add)
