num = int(input())

str_num = str(num)
first_digit = int(str_num[0])

if (num > 50 and num < 100) or first_digit == 7:
    print(True)
else:
    print(False)
