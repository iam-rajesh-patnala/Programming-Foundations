def create_matrix(rows):
    matrix = []     # 1 4 3 
                    # 5 0 2
                    # 2 2 8
    for i in range(rows):
        matrix.append(list(map(int, input().split())))
    return matrix


# -------------------------------------------
def create_temp_matrix(matrix):
    temp_matrix = []
    for row in matrix:
        temp_matrix.append(row.copy())
    return temp_matrix


# -------------------------------------------
def set_row(temp_matrix, i):
    for col_index in range(len(temp_matrix[0])):
        temp_matrix[i][col_index] = 0


# -------------------------------------------


def set_col(temp_matrix, j):
    for row_index in range(len(temp_matrix)):
        temp_matrix[row_index][j] = 0


# -------------------------------------------
def get_neighbour_sum(matrix, i, j):
    sum_of_neighbour = 0
    matrix_length = len(matrix)
    matrix_row_length = len(matrix[0])
    if i - 1 >= 0:
        sum_of_neighbour += matrix[i - 1][j]
    if i + 1 < matrix_length:
        sum_of_neighbour += matrix[i + 1][j]
    if j - 1 >= 0:
        sum_of_neighbour += matrix[i][j - 1]
    if j + 1 < matrix_row_length:
        sum_of_neighbour += matrix[i][j + 1]
    return sum_of_neighbour


# -------------------------------------------


def replace_zeros(matrix, temp_matrix, rows, columns):
    neighbour_sum_dict = dict()
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 0:
                set_row(temp_matrix, i)
                set_col(temp_matrix, j)
                neighbour_sum_dict[(i, j)] = get_neighbour_sum(matrix, i, j)
    for each_item in neighbour_sum_dict:
        temp_matrix[each_item[0]][each_item[1]] = neighbour_sum_dict.get(each_item)
    return temp_matrix


# -------------------------------------------
# def print_temp_matrix(changed_matrix, rows, columns):
#     for i in range(rows):
#         row = ""
#         for j in range(columns):
#             row += str(changed_matrix[i][j]) + " "
#         print(row)


# -------------------------------------------
def root():
    rows, columns = map(int, input().split())       # 3 3
    matrix = create_matrix(rows)
    temp_matrix = create_temp_matrix(matrix)
    changed_matrix = replace_zeros(matrix, temp_matrix, rows, columns)  
    for i in range(rows):
        val = changed_matrix[i]
        print(*val)     # 1 0 3
                        # 0 13 0
                        # 2 0 8
    # print_temp_matrix(changed_matrix, rows, columns)


root()
