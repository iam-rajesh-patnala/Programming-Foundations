starter = int(input())
row_input = int(input())


count = starter - 1
for i in range(row_input + 1):
    count += i

next_count = count

for j in range(1, row_input + 1):
    result = ""
    if j == 1:
        for k in range(row_input):
            result += str(count - k) + " "
            next_count -= 1
        print(result)
    elif j == row_input:
        left_spaces = "  " * (row_input - 1)
        result += left_spaces + str(starter) + " "
        print(result)
    else:
        left_spaces = "  " * (j - 1)
        hollow_space = "  " * (row_input - j - 1)
        first_num = next_count
        next_count -= row_input - j - 1
        result = left_spaces + str(first_num) + " " + hollow_space + str(next_count - 1) + " "
        next_count -= 2
        print(result)
