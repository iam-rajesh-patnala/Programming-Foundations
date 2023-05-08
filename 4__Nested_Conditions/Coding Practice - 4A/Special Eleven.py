number = int(input())

is_multiple_of_11 = (number % 11) == 0

is_one_more_multiple_of_11 = (number % 11) == 1

result = is_multiple_of_11 or is_one_more_multiple_of_11

if result:
    print("Special Eleven")
else:
    print("Normal Number")