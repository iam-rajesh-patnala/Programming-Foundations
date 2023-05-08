def is_prime(number):
    # complete this function
    is_prime_number = "Prime Number"
    if number <= 1:
        return "Not a Prime Number"
    else:
        for num in range(2, number):
            if number % 2 == 0:
                is_prime_number = "Not a Prime Number"
        return is_prime_number


number = int(input())
result = is_prime(number)
print(result)
