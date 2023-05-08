number1 = int(input())

is_multiple_of_9 = (number1 % 9) == 0

str_number = str(number1)
first_digit = int(str_number[0])
second_digit = int(str_number[1])

one_of_digit_nine = (first_digit == 9 or second_digit == 9)

result = is_multiple_of_9 or one_of_digit_nine

if result:
    print("Lucky Number")
else:
    print("Unlucky Number")