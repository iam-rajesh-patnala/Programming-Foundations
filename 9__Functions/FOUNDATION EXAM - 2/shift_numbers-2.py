def input_word(word):
    numbers = ""
    alphabets = ""
    for char in word:
        if char.isdigit():
            numbers += char
        else:
            alphabets += char
    order_word = numbers + alphabets
    return order_word


word = input()
input_word(word)
output = input_word(word)
print(output)
