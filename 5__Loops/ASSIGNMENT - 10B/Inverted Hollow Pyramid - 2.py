num = int(input())

spaces = "  "
hallow_space = "  "
count = 0

for i in range(1, num * 2):
    if i == 1 or i == (num * 2) - 1:
        left_spaces = spaces * (num - 1)
        result = left_spaces + str("1 ")
        print(result)
    elif i <= num:
        left_spaces = spaces * (num - i)
        count += 1
        hallow_spaces = hallow_space * (i - 2)
        result = left_spaces + str(i + 1 - 1) + " " + hallow_spaces + str(i + 1 - 1) + " "
        print(result)
    else:
        left_spaces =  ((num) - count ) * spaces
        hallow_spaces = hallow_space * (count - 2)
        result = left_spaces + str(count) + " " + hallow_spaces + str(count) + " "
        count -= 1
        print(result)