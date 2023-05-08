word = input()

result = [char for char in word if char.isalpha()]

print(''.join(result))