num1 = int(input())
num2 = int(input())


for i in range(num2):
    result = ""
    for j in range(num2):
        result += str(num1 + j) + " "
    print(result)
