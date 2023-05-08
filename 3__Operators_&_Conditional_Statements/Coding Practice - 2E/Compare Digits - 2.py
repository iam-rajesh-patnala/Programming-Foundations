number = input()
one_digit = number[0]
two_digit = number[1]

one_digit = int(one_digit)
two_digit = int(two_digit)

is_grater_than_ = (one_digit > two_digit) and (two_digit < one_digit)

is_grater_than_25 = (int(number) > 25) and is_grater_than_

print(is_grater_than_25)
