number = int(input())

is_divisible_by_6 = (number % 6) == 0
is_divisible_by_3 = (number % 3) == 0
is_divisible_by_2 = (number % 2) == 0

if is_divisible_by_6:
    print("Number is divisible by 6")
elif is_divisible_by_3:
    print("Number is divisible by 3")
elif is_divisible_by_2:
    print("Number is divisible by 2")
else:
    print("Number is not divisible by 2, 3 or 6")