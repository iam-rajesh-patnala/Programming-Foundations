password = input()

is_digit_contain = False
is_digit_uppercase = False

for character in password:
    is_digit = character.isdigit()
    is_digit_upper = character == character.upper()
    if is_digit:
        is_digit_contain = True
    if is_digit_upper:
        is_digit_uppercase = True


if is_digit_contain or is_digit_uppercase:
    print("Valid Password")
else:
    print("Invalid Password")
