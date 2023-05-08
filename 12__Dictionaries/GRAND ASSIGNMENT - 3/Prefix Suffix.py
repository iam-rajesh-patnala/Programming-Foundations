word_1 = input()
word_2 = input()

count = 1
neg_count = -1
matched_string = ""
condition = False


for i in range(len(word_2)):
    if word_2[:count] == word_1[neg_count:]:
        matched_string += word_2[:count]
        condition = True
        break
    else:
        count += 1
        neg_count -= 1

if condition:
  print(matched_string)
else:
  print("No overlapping")
