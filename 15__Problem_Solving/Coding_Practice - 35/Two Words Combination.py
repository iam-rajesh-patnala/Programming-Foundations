word = list(input().split())
word_length = len(word)

A = []

for i in range(word_length -1):
    A.append(sorted([word[i], word[i + 1]]))

for j in range(word_length):
    for k in range(j+2, word_length):
        word = sorted([word[j], word[k]])
        if word not in A:
            A.append(word)


for words in sorted(A):
    print(*words)


"""
# StackOverflow


user_str = input()
words = user_str.split()
words_result = []
words_adjacent =[]

for i in range(len(words)-1):
    words_adjacent.append(sorted([words[i],words[i+1]]))
    
    
for i in range(len(words)):
    for j in range(i+2,len(words)):
        word = sorted([words[i],words[j]])
        if word not in words_result and word not in words_adjacent :
            words_adjacent.append(word)

if words_adjacent:
    for item in sorted(words_adjacent):
        print(*item)
else:
    print("No Combinations")


"""
