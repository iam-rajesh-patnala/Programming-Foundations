password = input()

contains_digit = False

for character in password:
    is_digit = character.isdigit()
    if is_digit:
        contains_digit = True


is_all_lower = password.lower() == password
is_all_upper = password.upper() == password

contains_lower_and_upper = (not is_all_lower) and (not is_all_upper)
is_valid_password = contains_digit and contains_lower_and_upper

if contains_lower_and_upper and contains_digit:
    print("Valid Password")
else:
    print("Invalid Password")
