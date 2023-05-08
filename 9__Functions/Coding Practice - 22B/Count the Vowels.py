def count_the_vowels(word):
    vowels_count = 0
    for char in word:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            vowels_count += 1
    print(vowels_count)


word = input()
count_the_vowels(word)
