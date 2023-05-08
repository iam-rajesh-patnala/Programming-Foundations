col = int(input())
row = int(input())

val = ""
for i in range(1, col + 1):
    val = (str(i) + " ") * row
    print(val)
