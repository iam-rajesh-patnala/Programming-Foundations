row, col = input().split()

row = int(row)
col = int(col)


new_matrix = []

for i in range(row):
  matrix = input().split()
  matrix = list(map(int, matrix))
  new_matrix.extend(matrix)

new_matrix =  sorted(new_matrix)


count = 0
for j in range(row):
  row = ""
  for k in range(col):
    row += str(new_matrix[count]) + " "
    count+= 1
  print(row)


