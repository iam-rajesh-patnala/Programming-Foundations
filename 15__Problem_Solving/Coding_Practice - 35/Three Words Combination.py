""" 1st method """

word = input().split()
word.sort()

length = len(word)

combinations = []

for i in range(length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            three_words = word[i] + " " + word[j] + " " + word[k]
            combinations.append(three_words)

remove_duplicates = set(combinations)

converting_to_list = list(remove_duplicates)

sorted_list = sorted(converting_to_list)


for item in sorted_list:
    print(item)


""" 2nd method"""
word = input().split()
word.sort()

combinations = []

for i in range(len(word)):
    for j in range(i + 1, len(word)):
        for k in range(j + 1, len(word)):
            three_words = word[i] + " " + word[j] + " " + word[k]
            if three_words not in combinations:
                combinations.append(three_words)

for item in combinations:
    print(item)


""" 3rd method"""

word = input().split()
word.sort()

length = len(word)

combinations = []

for i in range(length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            three_words = [word[i], word[j], word[k]]
            if three_words not in combinations:
                combinations.append(three_words)

for item in combinations:
    print(*item)
