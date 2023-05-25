def get_repeated_digits(pin):
    repeated_digits =[]
    for each_num in pin:
        if pin.count(each_num) > 1 and each_num not in repeated_digits:
            repeated_digits.append(each_num)
    count = len(repeated_digits)
    return count
    


def root():
    pin = input()
    print(get_repeated_digits(pin))

root()