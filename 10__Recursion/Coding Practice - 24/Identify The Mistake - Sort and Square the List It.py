list_a = input().split(",")
list_x = []

for num in list_a:
    list_x += [int(num) ** 2]

print(sorted(list_x))
