def max_min_sum(matrix_list):
  min_list = []
  max_list = []
  sum_list = []
  for row in matrix_list:
    min_list.append(min(row))
    max_list.append(max(row))
    sum_list.append(sum(row))
  print(max_list)
  print(min_list)
  print(sum_list)

row_num, col_num = input().split()
row_num, col_num = int(row_num), int(col_num)

matrix_list = []

for matrix in range(row_num):
  matrix_row = input().split()
  matrix_row = list(map(int, matrix_row))
  matrix_list.append(matrix_row)

result = max_min_sum(matrix_list)


