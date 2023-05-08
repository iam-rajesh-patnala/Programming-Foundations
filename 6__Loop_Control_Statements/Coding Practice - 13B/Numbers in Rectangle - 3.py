num1 = int(input())
num2 = int(input())

starting_digit = num1 * num2

for i in range(num1):
    result = ""
    for j in range(num2):
        result += str(starting_digit) + " "
        starting_digit -= 1
    print (result)