num1 = input().split()
num2 = input().split()
num3 = input().split()

set_num1 = set(map(int, num1))
set_num2 = set(map(int, num2))
set_num3 = set(map(int, num3))

common = set_num1 & set_num2 & set_num3
print(sorted(list(common)))
