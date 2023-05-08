row, col = input().split()
row, col = int(row), int(col)

matrix = []

for i in range(row):
    mat = input().split()
    matrix.append(list(map(int, mat)))

for i in range(row):
    for j in range(col):
        if (i != j) and (i+j+1 != col):
            matrix[i][j] = 0

for mat in matrix:
    print(*mat)