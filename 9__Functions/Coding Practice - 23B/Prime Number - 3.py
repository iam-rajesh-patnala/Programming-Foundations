def is_prime(number):
    # complete this function
    is_prime_number = "Prime Number"
    
    for num in range(2, number):
        if number % num == 0:
            is_prime_number = "Not a Prime Number"
    return is_prime_number
            


number = int(input())   # 13
result = is_prime(number)   # call is_prime function
print(result)   # Prime Number