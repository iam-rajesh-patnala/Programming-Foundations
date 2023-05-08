def get_index(numbers_list, number, index=0):
    """first-method"""
    # return numbers_list.index(str(number))


    """second-method"""
    # for i in range(len(numbers_list)):
    #     if numbers_list[i] == str(number):
    #         return i


    """third-method"""
    if not numbers_list:
        return "Number not in list"
    elif numbers_list[0] == str(number):
        return index
    else:
        
        return get_index(numbers_list[1:], number, index+1)

numbers_list = input().split() # 10 20 30 40 50
number = int(input())   # 40


number_index = get_index(numbers_list, number)  # Call the get_index function

print(number_index)  # 3

