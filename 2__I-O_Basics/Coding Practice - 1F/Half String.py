username = input()
length = len(username)
last_index = int(length) - int(length / 2)
first_half = username[0:last_index]
print(first_half)
