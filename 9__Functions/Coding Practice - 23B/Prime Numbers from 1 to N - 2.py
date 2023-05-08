# write a program for prime numbers 8# initialize variables
def check_primes(number):
    if (number <= 1):
        return False
    
    for i in range(2, number):
        if (number % i == 0):
            return False
        

    return True

number = int(input())    # 8

primes = []

for i in range(1, number+1):
    if (check_primes(i)):
        primes.append(str(i))

print(" ".join(primes))     # 2 3 5 7


# def is_prime(n):
#     # complete this function
#     primes = []
#     for num in range(2, n+1):
#         if all(num%i != 0 for i in range(2, num)):
#             primes += [str(num)]
#     return " ".join(primes)
            

# n = int(input())

# # call the is_prime function
# print(is_prime(n))


