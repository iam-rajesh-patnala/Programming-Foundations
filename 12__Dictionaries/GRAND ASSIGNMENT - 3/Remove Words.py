sentence = input().split()

copy_sentence = sentence.copy()
num = int(input())

new_sentence = ""

for word in sentence:
  if len(word) == num:
    copy_sentence.remove(word)
  else:
    new_sentence+= word + " "
  
print(new_sentence)