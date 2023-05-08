num = int(input())
rows = int(input())

counter = 0

for i in range(1, rows + 1):
    if i == 1:
        first_row = str(num) + " "
        counter += 1
        print(first_row)

    elif i == rows:
        result = ""
        for j in range(1, rows + 1):
            result += str(num + counter) + " "
            counter += 1
        print(result)
    else:
        each_row = str(num + counter) + " "
        hollow_space_count = i - 2
        hollow_space = "  " * hollow_space_count
        each_row += hollow_space
        counter += 1
        each_row += str(num + counter)
        counter += 1
        print(each_row)
