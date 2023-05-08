def is_between_200_and_500(number):
    if 200 < number < 500:
        return "Yes"
    else:
        return "No" 
    #complete this function
    

number = int(input())

#call the is_between_200_and_500 function

print(is_between_200_and_500(number))