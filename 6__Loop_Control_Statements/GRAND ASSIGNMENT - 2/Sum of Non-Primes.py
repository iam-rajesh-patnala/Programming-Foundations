num1 = int(input())


count = 0
fin = 0
for i in range(num1):
    num2 = int(input())
    for j in range(2, num2):
        if num2 % j == 0:
            fin = fin + num2
            break
print(fin)
