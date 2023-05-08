"""
num_list = input().split()

new_list = set()

for num in num_list:
    count = num_list.count(num)
    if count % 2 != 0:
        new_list.add(int(num))
sort = sorted(new_list)
print(sort)
"""

num_list = list(map(int, input().split()))

new_list = []

for num in num_list:
    count = num_list.count(num)
    if count % 2 != 0:
        if num not in new_list:
            new_list.append(num)

sort = sorted(new_list)
print(sort)
