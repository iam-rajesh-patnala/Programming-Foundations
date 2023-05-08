num = int(input())

str_num = str(num)

length = len(str_num)

condition = False

for i in range(length):
    first = str_num[i]
    first = int(first)
    if first == 6 or first > 4:
        condition = True
print(condition)
