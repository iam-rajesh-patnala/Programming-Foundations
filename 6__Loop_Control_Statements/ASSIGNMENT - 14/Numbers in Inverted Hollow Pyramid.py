starter = int(input())
row = int(input())

next_starter = starter + row
counter = 0
for i in range(1, row + 1):
    result = ""
    if i == 1:
        for j in range(row):
            result += str(starter + j) + " "
            counter += 1
        print(result)
    elif i < row:
        left_spaces = " " * (i - 1)
        first_num = next_starter
        second_num = next_starter + (row - i)
        hollow_spaces_count = (second_num - first_num) - 1
        hollow_spaces = "  " * hollow_spaces_count
        result = (
            left_spaces + str(first_num) + " " + hollow_spaces + str(second_num) + " "
        )
        next_starter = second_num + 1
        counter -= 2
        print(result)
    else:
        left_spaces = " " * (row - 1)
        result = left_spaces + str(next_starter) + " "
        print(result)
