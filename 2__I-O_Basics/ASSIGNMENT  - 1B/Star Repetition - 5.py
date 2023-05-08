word_1 = input()
word_2 = input()
length = len(word_2)
king = length * "*"
king = king + word_1[length:]

print(king)
