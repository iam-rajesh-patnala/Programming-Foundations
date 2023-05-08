num1 = int(input())
num2 = int(input())
string_1 = str(num1)
string_2 = str(num2)

first = int(string_1[0])
last = int(string_2[-1])

if first < last:
    print(True)
else:
    print(False)