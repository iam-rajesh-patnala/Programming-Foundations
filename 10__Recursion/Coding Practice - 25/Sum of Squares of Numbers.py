def get_square_value(num):
    return num * num


def get_sum_of_squares(numbers):
    # Complete this function by calling get_sum_of_squares function
    total = 0

    for char in numbers:
        total += get_square_value(int(char))

    return total


numbers = input().split()  # 5 2 4

squares_sum = get_sum_of_squares(numbers)  # Call the get_sum_of_squares function
print(squares_sum)
