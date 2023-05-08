number = input()
length = len(number)

first_num = number[0]
second_num = number[1]
third_num = number[2]

mul = (int(first_num)**length) + (int(second_num)**length) + (int(third_num)**length)

if mul == int(number):
    print("True")
else:
    print("False")