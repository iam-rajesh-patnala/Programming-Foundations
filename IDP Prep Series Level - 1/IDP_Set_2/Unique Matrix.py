def check_unq_matrix(matrix, num_list):
    row_status = True
    column_status = True
    for each_row in matrix:
        for num in each_row:
            if each_row.count(num) > 1 or num not in num_list:
                row_status = False
                break

    # for each_column in zip(*matrix):
    #     for num in each_column:
    #         if each_column.count(num) > 1 or num not in num_list:
    #             column_status = False
    #             break

    for i in range(len(matrix)):
        column_list = []
        for j in range(len(matrix[i])):
            column_list.append(matrix[j][i])
        if column_list.count(column_list[i]) > 1 or column_list[i] not in num_list:
            column_status = False
            break

    print(row_status and column_status)


def get_matrix(loop):
    matrix = []
    for _ in range(loop):
        matrix.append(list(map(int, input().split())))
    num_list = [i for i in range(1, loop + 1)]
    check_unq_matrix(matrix, num_list)


def root():
    loop = int(input())
    get_matrix(loop)


root()


# =============================
