num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
num = input().split()
num = list(map(int, num))
num = set(num)
mul = num_set - num
mul = list(mul)
mul.sort()

print(mul)
