def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def get_fibonacci_series(n):
    list_a = []
    for i in range(n):
        list_a += [fibonacci(i)]
    return list_a


n = int(input())
result = get_fibonacci_series(n)
print(result)
