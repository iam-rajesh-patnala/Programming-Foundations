def word_rotation(word, vowels):

    result = []
    for i in range(len(word)):
        if word[i] in vowels:
            result.append(word[i:])
        else:
            result.append(word[i])
    return result


def check_vowels_in_word(normal_word, vowels):
    rotation_word = []
    vowels_not_in_list = True
    for word in normal_word:
        for char in list(word):
            if char in vowels:
                vowels_not_in_list = False
        if vowels_not_in_list:
            rotation_word.append(word)
        else:
            val = word_rotation(word, vowels)
            rotation_word.extend(val)
        
                

    print(*rotation_word)
normal_word = input().split()
vowels = ["a","e","i","o","u"]
check_vowels_in_word(normal_word, vowels)