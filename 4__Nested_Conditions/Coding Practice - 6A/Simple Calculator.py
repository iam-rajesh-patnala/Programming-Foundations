character = input()
num1 = int(input())
num2 = int(input())

add = character == "+"
sub = character == "-"
mul = character == "*"
div = character == "/"
mod = character == "%"

if add:
    addition = num1 + num2
    print(addition)
elif sub:
    subtraction = num1 - num2
    print(subtraction)
elif mul:
    multiplication = num1 * num2
    print(multiplication)
elif div:
    division = num1 / num2
    print(division)
elif mod:
    modulus = num1 % num2
    print(modulus)
