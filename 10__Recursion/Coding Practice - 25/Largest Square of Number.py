def get_squared_value(num):
    return num * num

def get_largest_square(numbers):
    # Complete this function
    largest = int(numbers[0]) * int(numbers[0])
    for char in numbers:
        square = get_squared_value(int(char))
        if square > largest:
            largest = square
            
    return largest

numbers = input().split()

result = get_largest_square(numbers) # call the get_largest_square function
print(result)