a = int(input())  # 1
b = int(input())  # -5
c = int(input())  # 6

root_1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
root_2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)

print(round(root_1, 2))  # 3.0
print(round(root_2, 2))  # 2.0
