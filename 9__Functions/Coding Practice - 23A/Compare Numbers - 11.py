def compare_numbers(first_number, second_number):
    return first_number > 100 and second_number > 100 and first_number < second_number
    
    

first_number = int(input())     # 105
second_number = int(input())    # 250

is_true = compare_numbers(first_number, second_number)# Call the compare_numbers function

print(is_true)  # True