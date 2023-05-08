


num_list = input().split(",")

number = ""
high_count = 0

for num in num_list:
    val = num_list.count(num)
    if val > high_count:
        high_count = val
        number = num

print(number)


