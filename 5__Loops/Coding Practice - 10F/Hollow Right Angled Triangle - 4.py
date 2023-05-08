num = int(input())


for i in range(1, num + 1):
    right_space_count = num - i
    right_space = right_space_count * " "
    if i == 1:
        result = "# " * num
        print(result)
    elif i == num:
        result = "+ "
        print(result)
    else:
        hallow_space_count = num - i - 1
        hallow_space = "  " * hallow_space_count
        result = "+ " + hallow_space + "+ "
        print(result)
