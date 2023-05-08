row = int(input())
col = int(input())

alphabets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

count = 0
for i in range(row):
    row_op = ""
    if i == 0 or i == row - 1:
        for j in range(col):
            row_op += alphabets[count].upper() + " "
            count += 1
        print(row_op)
    else:
        hollow_space = "  " * (col - 2)
        first_row = alphabets[count].upper() + " "
        count += 1
        end_row = alphabets[count + len(hollow_space) // 2].upper() + " "
        count += len(hollow_space) // 2 + 1
        print(first_row + hollow_space + end_row)
