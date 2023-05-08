num = int(input())

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = ""
for i in range(num):
    index = alpha[i] + " "
    result += index
    print(result)
