list_a = input().split()
list_b = input().split()

extended_list = []
condition = len(list_a) == len(list_b)

    
for i in range(len(list_a)):
    # extended_list.append(list_a[i])
    # extended_list.append(list_b[i])
    extended_list.extend([list_a[i]] + [list_b[i]])

if condition:
    print(extended_list)