def transpose(int_list, row, col):
  new_transpose = []

  for i in range(col):
    rows = []
    for j in range(row):
      miss = int_list[j][i]
      rows.append(miss)
    new_transpose.append(rows)
  return new_transpose


def converting_int(row):
    new_lits = []
    for char in row:
        char = int(char)
        new_lits.append(char)
    return new_lits


row, col = input().split()
row, col = int(row), int(col)
int_list = []

for rows in range(row):
    row_list = input().split()
    row_list = converting_int(row_list)
    int_list.append(row_list)

result = transpose(int_list, row, col)

for row_list in result:
  print(row_list)