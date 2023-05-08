def get_transpose_of_matrix_function(matrix, m, n):
    transpose = []
    for i in range(n):
        add = []
        for j in range(m):
            mis = matrix[j][i]
            add.append(mis)
        transpose.append(add)
    return transpose


def print_max_min_sum_for_row_wise_function(num_list, result_transpose):
    max_list = []
    min_list = []
    sum_list = []
    for lists in result_transpose:
        max_list.append(max(lists))
        min_list.append(min(lists))
        sum_list.append(sum(lists))

    print(max_list)
    print(min_list)
    print(sum_list)


def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)


result_transpose = get_transpose_of_matrix_function(num_list, m, n)
print_max_min_sum_for_row_wise_function(num_list, result_transpose)
