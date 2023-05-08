def calculate_percentage(number):
    if number <= 500:
        val = (5/100) * number 
        return val
    else:
        val = (10/100) * number
        return val
    
    # complete this function



number = int(input())

result = calculate_percentage(number) # Call the calculate_percentage function

print(result)