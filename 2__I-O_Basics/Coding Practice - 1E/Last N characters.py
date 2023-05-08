word = input()
num = int(input())
length = len(word)
king = length - num
half_word = word[king:]
print(half_word)
