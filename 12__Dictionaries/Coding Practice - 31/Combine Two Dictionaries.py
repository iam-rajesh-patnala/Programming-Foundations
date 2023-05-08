def function(keys_1, values_1):
    dict_final = {}
    for i in range(len(keys_1)):
        key = keys_1[i]
        value = int(values_1[i])
        dict_final[key] = value
    return dict_final


def function_2(keys_2, values_2):
    result = function(keys_1, values_1)
    for i in range(len(keys_2)):
        key = keys_2[i]
        value = int(values_2[i])
        result[key] = value
    return result


keys_1 = input().split()
values_1 = input().split()

keys_2 = input().split()
values_2 = input().split()

result = function(keys_1, values_1)
result_2 = function_2(keys_2, values_2)
result_2 = list(result_2.items())
result_2.sort()

print(result_2)
