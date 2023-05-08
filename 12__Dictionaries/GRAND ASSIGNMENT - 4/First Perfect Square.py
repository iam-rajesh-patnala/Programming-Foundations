m = int(input())
n = int(input())


perfect_square = []

for i in range(2, n+1):
  for j in range(m, n+1):
    if i*i == j:
      perfect_square.append(j)
print(perfect_square)
if len(perfect_square) > 0:
  print(perfect_square[0])
else:
  print("No Perfect Square")