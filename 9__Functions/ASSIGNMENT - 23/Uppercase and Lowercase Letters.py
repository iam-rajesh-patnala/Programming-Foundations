def get_lower_and_upper_case_letters(word):
    upper_case = ""
    lower_case = ""
    for char in word:
        if char.isdigit():
            continue
        elif char == char.upper():
            upper_case += char
        else:
            lower_case += char
    print(upper_case)
    print(lower_case)


word = input()
get_lower_and_upper_case_letters(word)
