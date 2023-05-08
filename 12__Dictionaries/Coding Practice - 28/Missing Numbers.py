# def int_conversion(str_input):
#     null_list = []
#     range_list = []
#     for num in str_input:
#         int_num = int(num)
#         null_list += [int_num]
#     for i in range(1, null_list[-1]+1):
#         range_list += [i]
#     set_a = set(null_list)
#     set_b = set(range_list)
#     compare = set_b - set_a
#     print(sorted(list(compare)))

# str_input = input().split()
# int_conversion(str_input)

num = input().split()
int_num = list(map(int, num))
max_num = int_num[-1]

first_list = set(range(1, max_num))
second_list = set(int_num)

diff = first_list - second_list
res = sorted(list(diff))
print(res)
