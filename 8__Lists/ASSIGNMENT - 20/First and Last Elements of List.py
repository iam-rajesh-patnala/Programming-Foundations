num = int(input())

total_list = []

for i in range(num):
    list_items = input()
    total_list += [int(list_items)]

first_two = total_list[:2]
last_two = total_list[num - 2 :]

print(first_two + last_two)
