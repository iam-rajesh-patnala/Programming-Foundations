num = input().split()


largest_num = int(num[0])

for i in num:
    if int(i) > largest_num:
        largest_num = int(i)
print(largest_num)
