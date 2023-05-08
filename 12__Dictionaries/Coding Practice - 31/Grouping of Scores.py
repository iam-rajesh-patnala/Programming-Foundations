def function(dict_list):
    new_dict = {}
    for item in dict_list:
        pair = item.split(":")
        key, value = pair
        if key in new_dict:
            new_dict[key] = new_dict[key] + int(value)
        else:
            new_dict[key] = int(value)
    return new_dict


dict_list = input().split(",")
dict_list.sort()
result = function(dict_list)
result = result.items()
list_a = []
for item in result:
    list_a.append(item)
print(list_a)
