number1 = int(input())
number2 = int(input())
number3 = int(input())

if number1 > number2:
    gratest = number1
else:
    gratest = number2
if number3 > gratest:
    gratest = number3
print(gratest)
