num1 = int(input())
num2 = int(input())


for i in range(num1):
    result = ""
    for j in range(num2):
        result += str(7+j) + " "
    print(result)