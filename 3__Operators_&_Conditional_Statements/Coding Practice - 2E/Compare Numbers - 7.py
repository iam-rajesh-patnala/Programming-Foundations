num = int(input())
str_num = str(num)

first_digits = str_num[:2]
last_digits = str_num[2:]

if int(first_digits) == 19 and (int(last_digits) > 30 and int(last_digits) < 60):
    print(True)
else:
    print(False)
