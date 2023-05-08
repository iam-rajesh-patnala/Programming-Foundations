sentence = input().split()

new_list = []
for char in sentence:
    if char[0] != "a":
        new_list += [char]

print(new_list)
