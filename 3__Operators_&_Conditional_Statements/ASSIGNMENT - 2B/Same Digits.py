num = int(input())
str_num = str(num)
first = int(str_num[0])
second = int(str_num[1])
third = int(str_num[2])

if first == second and second == third:
    print(True)
else:
    print(False)
