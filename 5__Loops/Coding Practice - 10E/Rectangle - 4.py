num1 = int(input())
num2 = int(input())

star = "* "
zero = "0 "

for i in range(1, num1 + 1):
    if i == 1 or i == num1:
        result = star * num2
        print(i, result)
    else:
        result = star + zero * (num2 - 2) + star
        print(i, result)
