"""def word_rotation(word, vowels):
    result = []
    for i in range(len(word)):
        if word[i] in vowels:
            result.insert(0, word[i:])
            break
        else:
            result.insert(1, word[i])

    print(*result, sep="", end=" ")


def check_vowels_in_word(normal_word, vowels):
    rotation_word = []
    for word in normal_word:
        vowels_not_in_list = True
        for char in list(word):
            if char in vowels:
                vowels_not_in_list = False
                break
        if vowels_not_in_list:
            rotation_word.append(word)
            print(*rotation_word, end=" ")
        else:
            val = word_rotation(word, vowels)
        vowels_not_in_list = True


normal_word = input().split()
vowels = ["a", "e", "i", "o", "u"]
check_vowels_in_word(normal_word, vowels)
"""



def trace_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    new_word = word
    for i in range(len(word)):
        if word[i].lower() in vowels:
            new_word = new_word[i:] + new_word[:i]
            break
    return new_word

def new_word(sentence):
    output = ""
    for word in sentence:
        new_word = trace_vowels(word)
        output += new_word + " "

    return output
        

def root():
    sentence = input().split()
    result = new_word(sentence)
    print(result)

root()