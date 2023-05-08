num = int(input())


for i in range(num):
    numbers = ""
    num = num - 1
    for j in range(1, num + 2):
        numbers = numbers + str(j) + " "
    print(numbers)
