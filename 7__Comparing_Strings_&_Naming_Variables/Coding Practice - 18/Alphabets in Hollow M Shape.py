num = int(input())

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

for i in range(num):
    if i == 0:
        spaces = " " * (num - (i + 1))
        val = spaces + (alphabets[i].upper()) + " " + spaces
        print(val * 2)
    else:
        spaces = " " * (num - (i + 1))
        hallow_spaces = " " * count
        val = spaces + (alphabets[i].upper()) + " " + hallow_spaces + (alphabets[i].upper()) + spaces + " "
        count += 2
        print(val * 2)

#-------------------------------------------------

rows = int(input())

for row in range(1, rows + 1):
    spaces = " " * (rows - row)
    
    if row == 1:
        each_row = spaces + (chr(row + 64 ) + " ") 
    else:
        hollow_spaces = "  " * (row - 2)
        each_row = spaces + (chr(row + 64) + " ") + hollow_spaces + (chr(row + 64) + " ")

    spaces_between_triangles = " " * (rows - row)
    
    print(each_row + spaces_between_triangles + each_row)