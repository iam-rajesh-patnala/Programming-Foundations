def sum_of_numbers(num_1, num_2):
    num_1_length, num_2_length = len(num_1), len(num_2)
    max_num_length = max(num_1_length, num_2_length)
    
    if num_1_length < max_num_length:
        num_1 = "0" * (max_num_length - num_1_length) + num_1
    elif num_2_length < max_num_length:
        num_2 = "0" * (max_num_length - num_2_length) + num_2

    carry_found = False

    for i in range(len(num_1)):
        if (int(num_1[i])) + int(num_2[i]) > 9:
            carry_found = True
            break
    return carry_found
        
def root():

    num_1, num_2 = input().split()
    carry_found = sum_of_numbers(num_1, num_2)

    if carry_found:
        print("Hard")
    else:
        print("Easy")
root()
