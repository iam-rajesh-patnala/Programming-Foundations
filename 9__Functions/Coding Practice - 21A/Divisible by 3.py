num_list = list(map(int, input().split()))

new_list = []

for num in num_list:
    if num % 3 == 0:
        # new_list.append(num)
        new_list += [num]

print(new_list)