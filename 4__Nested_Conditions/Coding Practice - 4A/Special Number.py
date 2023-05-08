number = int(input())

str_number = str(number)
str_number_1 = int(str_number[0])
str_number_2 = int(str_number[1])
sum_of_two_numbers_7 = (str_number_1 + str_number_2) == 7

one_of_digit_7 = (str_number_1 == 7 ) or (str_number_2 == 7 )

is_multiple_7 = (number % 7) == 0

if sum_of_two_numbers_7 or one_of_digit_7 or is_multiple_7:
    print("Special Number")
else:
    print("Normal Number")

