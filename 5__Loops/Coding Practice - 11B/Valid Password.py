password = input()

contains_digit = False

for character in password:
    is_digit = character.isdigit()
    if is_digit:
        contains_digit = True

if contains_digit:
    print("Valid Password")
else:
    print("Invalid Password")
