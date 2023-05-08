number1 = int(input())
number2 = int(input())

if (number1 == 6 or number2 == 6) or number1 + number2 == 6 or number1 - number2 == 6 or number2 - number1 == 6:
    print("Lucky")
else:
    print("Not Lucky")
