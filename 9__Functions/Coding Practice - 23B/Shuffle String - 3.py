def shuffle_string(string, indexes_list):
    # complete this function
    new_string = ""

    for num in indexes_list:
        new_string += string[int(num)]

    return new_string


string = input()        # tonyPh
indices_list = input()  # 4 3 0 5 1 2

result = shuffle_string(string, indices_list.split())  # call the shuffle_string function
print(result)            #Python
