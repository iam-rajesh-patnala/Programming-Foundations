num = int(input())


for i in range(1, num+1):
    result = ""
    for j in range(num):
        result += str(num-j) + " "
    print(result) 