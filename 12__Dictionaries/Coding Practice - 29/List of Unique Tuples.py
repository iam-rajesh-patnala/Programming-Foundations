def tracing_duplicate(total_list):
    length = len(total_list)
    new_list = []

    for i in range(length):
        nested_list_length = len(total_list[i])
        conv_list = list(set(total_list[i]))
        conv_list.sort()
        conv_list_length = len(conv_list)

        if conv_list_length == nested_list_length:
            new_list.append(conv_list)

    return new_list


# converting str_to_int_numbers


def converting_str_to_int(list_a):
    length = len(list_a)
    for i in range(length):
        list_a[i] = int(list_a[i])


total_list_range = int(input())
total_list = []
for i in range(total_list_range):
    list_a = input().split()
    converting_str_to_int(list_a)
    total_list.append(list_a)


result = tracing_duplicate(total_list)
print(result)
