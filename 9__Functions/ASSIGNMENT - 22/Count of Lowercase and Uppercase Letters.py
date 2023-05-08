def count_of_lowercase_and_uppercase_letters(arg_1):
    count_of_uppercase = 0
    count_of_lowercase = 0
    for char in arg_1:
        if char.isdigit():
            continue
        if char == char.upper():
            count_of_uppercase += 1
        elif char == char.lower():
            count_of_lowercase += 1

        # Complete this function

    print(count_of_uppercase)
    print(count_of_lowercase)


word = input()
# Call the count_of_lowercase_and_uppercase_letters function
count_of_lowercase_and_uppercase_letters(word)
