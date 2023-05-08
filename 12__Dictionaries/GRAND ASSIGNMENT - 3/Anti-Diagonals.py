row, col = input().split()
row, col = int(row), int(col)
total_matrix = []

for mat in range(row):
    matrix = input().split()
    matrix = list(map(int, matrix))
    total_matrix.append(matrix)

max_sum = row + col - 2
for sum in range(max_sum+1):
    for i in range(sum+1):
        if i < row and sum - i < col:
            print(total_matrix[i][sum - i], end=" ")
    print()