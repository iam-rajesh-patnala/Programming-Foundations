input_word = input().split()
input_word = sorted(input_word)
print(input_word)

new_dict = dict()

for word in input_word:
  if word in new_dict:
    new_dict[word] += 1
  else:
    new_dict[word] = 1

for name, value in new_dict.items():
  print("{}: {}".format(name,value))