row_col = int(input())

alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for i in range(row_col):
    result = ""
    for j in range(row_col):
        result += alphabets[j] + " "
    print(result)