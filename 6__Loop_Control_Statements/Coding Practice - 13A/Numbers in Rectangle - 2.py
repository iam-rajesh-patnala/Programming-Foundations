num1 = int(input())
num2 = int(input())

number = 1

for i in range(num1):
    add = ""
    for i in range(num2):
        add = add + str(number) + " "
        number = number + 1
    print(add)
