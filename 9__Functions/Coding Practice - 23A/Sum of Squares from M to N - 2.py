def sum_of_squares_m_to_n(m, n):
    total_sum_of_squares = 0
    for i in range(m, n + 1):
        total_sum_of_squares += i**2
    print(total_sum_of_squares)


m = int(input())
n = int(input())
sum_of_squares_m_to_n(m, n)
