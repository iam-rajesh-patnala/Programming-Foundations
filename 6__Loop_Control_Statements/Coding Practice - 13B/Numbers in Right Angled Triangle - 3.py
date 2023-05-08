num1 = int(input())
num2 = int(input())



for i in range(1, num2+1):
    numbers = ""
    for j in range(i):
        numbers = numbers + str(num1) + " "
        num1+= 1
    print(numbers)
        
