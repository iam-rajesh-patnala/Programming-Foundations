num1 = input().split(",")
num2 = input().split(",")
map_num1 = list(map(int, num1))
map_num2 = list(map(int, num2))

common = set(map_num1) & set(map_num2)
common = list(sorted(common))
print(common)
