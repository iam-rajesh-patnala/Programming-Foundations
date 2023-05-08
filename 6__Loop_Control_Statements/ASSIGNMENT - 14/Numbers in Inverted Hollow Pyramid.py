# starter = int(input())
# row = int(input())


# next_starter = starter + row
# counter = row
# for i in range(1, row+1):
#     result = ""
#     if i == 1:
#         for j in range(row):
#             result += str(starter + j) + " "
#         counter -= 2 
#         print(result)
#     elif i < row:
#         left_spaces = " " * (i-1)
#         first_num = next_starter
#         second_num = next_starter + (row-i)
#         hollow_spaces_count =  counter#second_num - first_num
#         hollow_spaces = " " * (hollow_spaces_count) + " " * (hollow_spaces_count // 2)
#         res = left_spaces + str(first_num) + " " + hollow_spaces + str(second_num) + " "
#         next_starter = second_num + 1
#         counter -= 2
#         print(res)
#     else:
#         left_spaces = " " * (row - 1)
#         res = left_spaces + str(next_starter) + " "
#         print(res


def compute_power(a, b):
    if(b == 0):
        return 1
    return a * compute_power(a, b-1)

a = int(input())
b = int(input())
result = compute_power(a, b)
print(result)