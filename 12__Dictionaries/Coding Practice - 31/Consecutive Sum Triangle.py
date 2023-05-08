def sum_of_two(num_list):
    final_list = []
    for i in range(len(num_list) - 1):
        pair = num_list[i] + num_list[i + 1]
        final_list.append(pair)
    return final_list


# def consecutive_sum(num_list):
#     for i in range(len(num_list) - 1):
#         sum_seq = sum_of_two(num_list)
#         num_list = sum_seq
#         print(sum_seq)


def consecutive_sum(num_list):
    while len(num_list) > 1:
        sum_seq = sum_of_two(num_list)
        num_list = sum_seq
        print(sum_seq)


num_list = input().split(",")
num_list = list(map(int, num_list))
print(num_list)
result = consecutive_sum(num_list)
