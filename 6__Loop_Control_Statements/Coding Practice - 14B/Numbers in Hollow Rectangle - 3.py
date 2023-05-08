row = int(input())

col = int(input())

starter = row * col

count = 0

for i in range(1, row + 1):
    result = ""
    if i == 1 or i == row:
        for j in range(col):
            result += str(starter) + " "
            starter -= 1
            count += 1
        print(result)

    else:
        each_digit = str(starter) + " "
        hollow_spaces_count = count - 2
        hollow_spaces = "  " * hollow_spaces_count
        each_digit += hollow_spaces
        each_digit += str(starter - (len(hollow_spaces) // 2 + 1)) + " "
        starter -= col
        print(each_digit)
