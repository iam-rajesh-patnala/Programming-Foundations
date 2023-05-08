num1 = int(input())
num2 = int(input())

result = ""

for num in range(num1, num2+1):
    if num % 6 == 0:
        result += (str(num) + " ")

if result == "":
    print("No Numbers Found")
else:
    print(result)