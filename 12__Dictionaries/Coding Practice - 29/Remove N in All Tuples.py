num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)]

length = len(num_list)
num = int(input())
new_list = []

for item in num_list:
    if num in item:
        index = item.index(num)
        new = item[:index] + item[index + 1 :]
        new_list.append(new)
    else:
        new_list.append(item)
print(new_list)
