list_a = [("apple", "banana", "orange", "grapes"), ("cricket", "football", "hockey"), ("car", "bicycle", "bus")]


num = int(input())

f_list = []

for i in range(num):
    indexes = input().split()
    t_index = int(indexes[0])
    l_index = int(indexes[1])
    f_list.append(list_a[t_index][l_index])

print(f_list)
