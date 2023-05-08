def max_square(matrix, col, row):
    res = [[0 for i in range(row + 1)] for j in range(col + 1)]
    side_length = 0
    for i in range(1, len(res)):
        for j in range(1, len(res[0])):
            if matrix[i - 1][j - 1] == "X":
                res[i][j] = min(res[i][j - 1], res[i - 1][j], res[i - 1][j - 1]) + 1
                side_length = max(side_length, res[i][j])
    return side_length * side_length


col, row = map(int, input().split())
matrix = []

for i in range(col):
    input_matrix = input().split()
    matrix.append(input_matrix)

function = max_square(matrix, col, row)

print(function)
