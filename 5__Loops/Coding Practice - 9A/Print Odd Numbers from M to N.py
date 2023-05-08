num1 = int(input())
num2 = int(input())

result = ""

for i in range(num1, num2+1):
    if i % 2 != 0:
        result+= str(i) + " "
print(result)