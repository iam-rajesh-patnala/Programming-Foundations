num = int(input())

for i in range(1, num+1):
    result = ""
    if i == 1 or i == num:
        for j in range(1, num+1):
            result += str(j) + " "
        print(result)
    else:
        result = str(1)+" " + ("  " * (num-2)) + str(num)
        print(result)
