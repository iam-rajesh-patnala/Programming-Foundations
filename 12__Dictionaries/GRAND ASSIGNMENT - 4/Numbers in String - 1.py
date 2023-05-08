sentence = input()

sum = 0
count = 0
for char in sentence:
  if char.isdigit():
    sum+= int(char)
    count+= 1
print(sum)
print(round(sum/count, 2))
