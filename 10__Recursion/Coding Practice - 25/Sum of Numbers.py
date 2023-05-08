def get_sum(numbers):
    each_num = int(numbers[0])

    if len(numbers) == 1:
        return each_num

    return each_num + get_sum(numbers[1:])

    # total = 0
    # for num in numbers:
    #     total += int(num)
    # return total


numbers = input().split()

sum_of_numbers = get_sum(numbers)

print(sum_of_numbers)
