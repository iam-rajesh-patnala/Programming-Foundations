def sum_of_cubes_m_to_n(m, n):
    total_sum = 0
    for i in range(m, n + 1):
        total_sum += i**3
    print(total_sum)


m = int(input())
n = int(input())
sum_of_cubes_m_to_n(m, n)
