sentence = input()

numbers = ""
alphabets = ""

for word in sentence:
    if word.isdigit():
        numbers += word
    else:
        alphabets += word

order = alphabets + numbers

print(order)
