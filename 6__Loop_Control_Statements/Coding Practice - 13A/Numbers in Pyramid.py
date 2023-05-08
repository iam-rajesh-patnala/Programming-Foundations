num1 = int(input())
num2 = int(input())


for i in range(1, num2+1):
    left_spaces = " " * (num2 - i)
    result = ""
    for j in range(i):
        result += str(num1+j) + " "
        
    print(left_spaces + result)