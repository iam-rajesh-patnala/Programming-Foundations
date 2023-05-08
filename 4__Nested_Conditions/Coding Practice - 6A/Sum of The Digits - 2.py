num = int(input())
str_num = str(num)

one_digit = len(str_num) == 1
two_digit = len(str_num) == 2
three_digit = len(str_num) == 3
four_digit = len(str_num) == 4
five_digit = len(str_num) == 5

if one_digit:
    print(num)
elif two_digit:
    one_digit = int(str_num[0])
    two_digit = int(str_num[1])
    print(one_digit + two_digit)
elif three_digit:
    one_digit = int(str_num[0])
    two_digit = int(str_num[1])
    three_digit = int(str_num[2])
    print(one_digit + two_digit + three_digit)
elif four_digit:
    one_digit = int(str_num[0])
    two_digit = int(str_num[1])
    three_digit = int(str_num[2])
    four_digit = int(str_num[3])
    print(one_digit + two_digit + three_digit + four_digit)
elif five_digit:
    one_digit = int(str_num[0])
    two_digit = int(str_num[1])
    three_digit = int(str_num[2])
    four_digit = int(str_num[3])
    five_digit = int(str_num[4])
    print(one_digit + two_digit + three_digit + four_digit + five_digit)
