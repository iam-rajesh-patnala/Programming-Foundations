def get_principal_diagonal_elements(matrix, m, n):

    new_list = []

    for i in range(n):
        matrix[i] = matrix[i][i]
        new_list.append(matrix[i])
    print(new_list)


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

get_principal_diagonal_elements(num_list, m, n)
