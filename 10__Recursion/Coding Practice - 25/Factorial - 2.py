def compute_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * compute_factorial(n - 1)


num = int(input())
result = compute_factorial(num)
print(result)
