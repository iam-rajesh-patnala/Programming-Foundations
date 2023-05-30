def create_matrix(rows):
    matrix = []     # X O X O O
                    # X O X X X
                    # X X X X X
                    # X O O X O
    for i in range(rows):
        matrix.append(input().split())
    return matrix
# ----------------------------------------------------------
def check_if_sub_matrix_contains_zero(matrix, i, j, k, l):
    for m in range(k + 1):
        for n in range(l + 1):
            if matrix[i + m][j + n] == "O":
                return True
    return False
# ----------------------------------------------------------
def get_max_sub_matrix_area(matrix, rows, columns, i, j):
    max_sub_matrix_area = 0
    for k in range(rows - i):
        for l in range(columns - j):
            is_sub_matrix_contains_zero = check_if_sub_matrix_contains_zero(matrix, i, j, k, l)

            if not is_sub_matrix_contains_zero:
                max_sub_matrix_area = max(max_sub_matrix_area, (k + 1) * (l + 1))
    return max_sub_matrix_area
# ----------------------------------------------------------
def get_max_area_of_rectangle(matrix, rows, columns):
    max_area_of_rectangle = 0
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == "X":
                max_sub_matrix_area = get_max_sub_matrix_area(matrix, rows, columns, i, j)
                max_area_of_rectangle = max(max_area_of_rectangle, max_sub_matrix_area)
    return max_area_of_rectangle
# ----------------------------------------------------------
def root():
    rows, columns = map(int, input().split())  # 4 5
    matrix = create_matrix(rows)
    max_area_of_rectangle = get_max_area_of_rectangle(matrix, rows, columns)
    print(max_area_of_rectangle)  # 6


root()
