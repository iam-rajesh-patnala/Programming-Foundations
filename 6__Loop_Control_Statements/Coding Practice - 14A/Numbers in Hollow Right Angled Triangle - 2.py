num = int(input())

spaces = "  "

count = 0

for i in range(1, num + 1):
    left_spaces = "  " * (num - i)
    result = ""
    last_digit = ""
    if i == 1:
        result = left_spaces + str(i)
        print(result)
    elif i == num:
        for j in range(num):
            result += str(num - j) + " "
        print(result)
    else:
        hallow_space = "  "
        result = left_spaces + (str(i)+" ") + hallow_space * (count-1) + str(1)
        print(result)
    count += 1
