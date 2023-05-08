def is_prime(num):
    total_primes = 0
    length = len(num)
    for i in range(0, length):
        index = int(num[i])
        prime = True
        for j in range(2, index):
            if index % j == 0:
                prime = False
                break
        if prime:
            total_primes += index
    return total_primes


input_word = input().split()
total = is_prime(num=input_word)
print(total)
