num = int(input())
str_num = str(num)

first = int(str_num[0])
second = int(str_num[1])
last = int(str_num[2])

first_grater_7 = (first > 7) and (second > 7) and (last > 7)

first_num = (first * second) <= 30
second_num = (second * last) <= 30
last_num = (last * first) <= 30

if first_grater_7:
    print(True)
elif first_num and second_num and last_num:
    print(True)
else:
    print(False)
