fruits = {"apples": 10, "bananas": 20, "mangoes": 15, "oranges": 200, "watermelons": 50}


def change_key(pairs, key_1, key_2):
    final_list = []
    for item in pairs:
        if key_1 in item:
            item = list(item)
            item[0] = key_2
            item = tuple(item)
            final_list.append(item)
        else:
            final_list.append(item)
    return final_list


key_1 = input()
key_2 = input()

pairs = fruits.items()
result = change_key(pairs, key_1, key_2)
print(result)


# above code is my own own approach


fruits = {"apples": 10, "bananas": 20, "mangoes": 15, "oranges": 200, "watermelons": 50}


# Write your code here
key = input()
new_key = input()
fruits_details = list(fruits.items())
fruits_details_copy = fruits_details.copy()


fruit_count = len(fruits_details)

for i in range(fruit_count):
    if fruits_details[i][0] == key:
        updated_tuple = (new_key, fruits_details[i][1])  # creating new tuple with new key and existing value
        fruits_details_copy[i] = updated_tuple  # assigning updated_tuple as reference to the fruits_details_copy
print(fruits_details_copy)
