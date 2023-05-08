def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []
total = 0

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)
    total += sum(list_a)

max_list = max(num_list)
min_list = min(num_list)
print(max(max_list))
print(min(min_list))
print(total)
