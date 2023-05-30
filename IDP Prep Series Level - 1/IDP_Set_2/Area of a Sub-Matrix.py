def get_product(mid_num):
    total = 1
    for num in mid_num:
        total *= num
    return total

def get_resultant(matrix, resultant):
    column_result = []
    row_result = []
    row_result.extend(matrix[resultant:-resultant])

    if not row_result:
        return 0
    else:
        for each_list in row_result:
            column_result.extend(each_list[resultant:-resultant])

    return get_product(column_result)
            

def get_matrix(col, row):
    matrix =[]
    for i in range(col):
        matrix.append(list(map(int, input().split())))
    
    return matrix

def root():
    col, row = map(int, input().split())
    matrix = get_matrix(col, row)
    resultant = int(input())
    print(get_resultant(matrix, resultant))


root()


# -------------------------------------------------------
def read_matrix(rows):
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix
def get_matrix_product(matrix):
    if len(matrix) == 0:
        return 0
    product = 1
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            product = product * matrix[i][j]
    return product
def get_sub_matrix(matrix, rows, columns, k):
    new_sub_matrix = []
    sub_matrix_rows = matrix[k:rows-k]
    for each_row in sub_matrix_rows:
        each_row = each_row[k:columns-k]
        new_sub_matrix.append(each_row)
    return new_sub_matrix
def main():
    rows, columns = map(int, input().split())
    matrix = read_matrix(rows)
    k = int(input())
    resultant_matrix = get_sub_matrix(matrix, rows, columns, k)
    product = get_matrix_product(resultant_matrix)
    print(product)

main()