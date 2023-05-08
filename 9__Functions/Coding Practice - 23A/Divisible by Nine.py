def check_divisible_by_9(first_number, second_number, third_number):
    return first_number % 9 == 0 or second_number % 9 == 0 or  third_number % 9 == 0 # Pro mode
    # complete this function
    

first_number = int(input())     # 6
second_number = int(input())    # 9
third_number = int(input())     # 16

result = check_divisible_by_9(first_number, second_number, third_number) # Call the check_divisible_by_9 function

print(result)      # True

# -------------------------------------

"""def check_divisible_by_9(first_number, second_number, third_number):
    if first_number % 9 == 0 or second_number % 9 == 0 or third_number % 9 == 0:
        return True
    else:
        return False
    # complete this function


first_number = int(input())  # 6
second_number = int(input())  # 9
third_number = int(input())  # 16

result = check_divisible_by_9(first_number, second_number, third_number)  # Call the check_divisible_by_9 function

print(result)  # True
"""