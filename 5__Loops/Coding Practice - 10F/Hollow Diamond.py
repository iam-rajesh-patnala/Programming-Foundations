num = int(input())

left_spaces_count = num - 1
left_spaces = " " * left_spaces_count
row_output = left_spaces + "*"
print(row_output)

count = -1

for i in range(2, num + 1):
    left_spaces_count = num - i
    left_spaces = " " * left_spaces_count
    count = count + 2
    hollow_spaces = " " * count
    row_output = left_spaces + "*" + hollow_spaces + "*"
    print(row_output)

for j in range(1, num - 1):
    left_spaces_count = j
    left_spaces = " " * left_spaces_count
    count = count - 2
    hollow_spaces = " " * count
    row_output = left_spaces + "*" + hollow_spaces + "*"
    print(row_output)

left_spaces_count = num - 1
left_spaces = " " * left_spaces_count
row_output = left_spaces + "*"
print(row_output)
