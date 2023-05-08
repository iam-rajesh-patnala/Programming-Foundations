num_list = sorted(list(map(int, input().split(","))), reverse=True)

first_five_num = sum(num_list[:5])

print(first_five_num)
