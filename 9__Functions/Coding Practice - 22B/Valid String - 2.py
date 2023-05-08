def valid_string(string):
    
    if len(string) >= 6 or string[0].isdigit():
        return "Valid String"
    else:
        return "Invalid String"
    # complete this function



string = input()

result = valid_string(string)   # Call the valid_string function

print(result)