num = int(input())

str_num = str(num)

first = str_num[0]
second = str_num[1]
last = str_num[2]

first = int(first)
second = int(second)
last = int(last)
sum = first + second + last

if sum < 12 and (first == 1 or second == 1) and last == 5:
    print(True)
else:
    print(False)
