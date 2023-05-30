def groot(matrix):
    total = 0
    for k in range(len(matrix)):
        if k == 0 or k == len(matrix) - 1:
            total += sum(matrix[k])
        else:
            total += matrix[k][0] + matrix[k][-1]
    return total


def matrix(row, col):
    matrix = []
    for i in range(row):
        matrix.append(list(map(int, input().split())))

    if len(matrix) < 3:
        total = 0
        for j in range(len(matrix)):
            total += sum(matrix[j])
        return total
    else:
        return groot(matrix)


row, col = map(int, input().split())


print(matrix(row, col))


# ------------------------------------------------------------------------------------

"""
def get_perimeter_of_matrix(matrix, rows, columns):
    sum_of_perimeter = 0
    for i in range(rows):
        for j in range(columns):
            if (i == 0) or (i == rows - 1) or (j == 0) or (j == columns - 1):
                sum_of_perimeter += matrix[i][j]
    return sum_of_perimeter


def read_matrix(rows):
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def main():
    rows, columns = map(int, input().split())
    matrix = read_matrix(rows)
    perimeter_of_matrix = get_perimeter_of_matrix(matrix, rows, columns)
    print(perimeter_of_matrix)

main()

"""