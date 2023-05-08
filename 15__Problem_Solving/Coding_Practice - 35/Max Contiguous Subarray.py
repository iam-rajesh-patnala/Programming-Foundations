num_list = list(map(int, input().split()))

length = len(num_list)

min_number = min(num_list)

max_sum_list = []

if length > 1:
    for i in range(length):
        for j in range(i, length):
            sub_list = num_list[i : j + 1]
            total = sum(sub_list)
            if total > min_number:
                min_number = total
                max_sum_list.append(sub_list)

    for nums in max_sum_list[-1]:
        print(nums, end=" ")

else:
    print(num_list[0])

