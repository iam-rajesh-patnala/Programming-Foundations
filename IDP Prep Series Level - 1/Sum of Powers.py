def get_sum_of_powers(base, power):
    return base ** power

def get_powers(num):
    total = 0
    for numbers in num:
        if len(numbers) > 1:
            base,power = int(numbers[:-1]), int(numbers[-1])
            total += get_sum_of_powers(base, power)
    print(total)


def root():
    num = input().split()
    get_powers(num)

root()