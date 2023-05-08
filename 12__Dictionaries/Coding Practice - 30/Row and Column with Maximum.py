def int_conv(row):
    new_list = []
    for char in row:
        char = int(char)
        new_list.append(char)
    return new_list


row_num, col_num = input().split()
row_num, col_num = int(row_num), int(col_num)

row_list = []

for i in range(row_num):
    row = input().split()
    conv = int_conv(row)
    row_list.append(conv)


max_num = []

for j in row_list:
    max_num.append(max(j))

max_number = max(max_num)
index = max_num.index(max_number)

row_max_list = row_list[index]
col_max = row_max_list.index(max_number)


col_max_list = []

for me in row_list:
    col_max_list.append(me[col_max])


print(row_max_list)
print(col_max_list)
