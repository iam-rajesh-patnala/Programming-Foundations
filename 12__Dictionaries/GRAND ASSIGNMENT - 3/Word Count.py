word = input().split()

new_dict = {}

for i in word:
    if i in new_dict:
        new_dict[i] += 1
    else:
        new_dict[i] = 1

for name, num in new_dict.items():
    formation = "{name}: {number}"
    result = formation.format(name=name, number=num)
    print(result)
