num1 = int(input())
num2 = int(input())

initiation = 0

for num in range(1, num2+1):
    initiation += num

count = initiation + num1 - 1

for i in range(num2):
    result = ""
    for j in range(num2-i):
        result+= str(count) + " "
        count -= 1
    print(result)