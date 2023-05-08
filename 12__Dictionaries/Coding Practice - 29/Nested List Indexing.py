num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]
num = int(input())
msg = "{out_index} {in_index}"

for i in range(len(num_list)):
    if num in num_list[i]:
        arg_2 = num_list[i].index(num)
        arg_1 = i

print(msg.format(out_index=arg_1, in_index=arg_2))
