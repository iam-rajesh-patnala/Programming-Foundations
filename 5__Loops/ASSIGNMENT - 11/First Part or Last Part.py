word = input()
word2 = input()

condition = False
if word[: len(word2)] == word2[: len(word2)]:
    condition = True

print("{}".format(condition))
