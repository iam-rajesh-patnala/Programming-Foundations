def is_prime(num):
    total_primes = 0
    for i in range(input_1, input_2 + 1):
        for j in range(2, input_1):
            if i % j == 0:
                break
        else:
            total_primes += i
    print(total_primes)


input_1 = int(input())
input_2 = int(input())
num = (input_1, input_2)
is_prime(num)
