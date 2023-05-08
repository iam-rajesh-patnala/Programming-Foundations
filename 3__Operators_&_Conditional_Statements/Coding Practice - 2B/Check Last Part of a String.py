word = input()
half_word = input()

length_word = len(word)
length_half_word = len(half_word)

new = word[-length_half_word:]

if half_word == new:
    print(True)
else:
    print(False)
