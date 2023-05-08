# # # Function to check if a number is prime or not
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num/2)+1):
#         if num % i == 0:
#             return False
#     return True

# # Taking input from user
# M = int(input())
# N = int(input())

# # Printing prime numbers between M and N
# # print("Prime numbers between", M, "and", N, "are:")
# for num in range(M, N+1):
#     if is_prime(num):
#         print(num)


def check_is_prime(m, n):
    primes = []
    for num in range(m, n + 1):
        flag = True
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break
        if flag:
            primes.append(str(num))
    return " ".join(primes)


m = int(input())
n = int(input())

prime_numbers = check_is_prime(m, n)

print(prime_numbers)
