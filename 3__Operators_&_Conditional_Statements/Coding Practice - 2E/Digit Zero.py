"""
num = int(input())
condition = False

for char in str(num):
    if int(char) == 0:
        condition = True

print(condition)

"""

num = int(input())

first_digit = str(num)[0]
second_digit = str(num)[1]
third_digit = str(num)[2]

if (int(first_digit) == 0) or (int(second_digit) == 0) or (int(third_digit) == 0):
    print(True)
else:
    print(False)
