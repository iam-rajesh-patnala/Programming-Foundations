num = int(input())

count = 0
for i in range(1, num * 2):
    if i == 1 or i == (num * 2) - 1:
        print("1 ")
    elif i <= num:
        hallow_space_count = i - 2
        count += 1
        hallow_space = "  " * hallow_space_count
        result = str(i) + " " + hallow_space + str(i)
        print(result)

    else:
        hallow_space_count = count - 2
        count -= 1
        hallow_space = "  " * hallow_space_count
        result = str((num * 2 - i)) + " " + hallow_space + str((num * 2 - i))
        print(result)
