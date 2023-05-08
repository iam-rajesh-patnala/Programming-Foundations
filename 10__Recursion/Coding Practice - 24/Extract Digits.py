def king():
    full_digits = []
    for char in word:
        if char.isdigit():
            full_digits += [int(char)]
    sum_digits = sum(full_digits)
    min_digits = min(full_digits)
    max_digit = max(full_digits)
    print(sum_digits)
    print(min_digits)
    print(max_digit)


word = input()
king()
