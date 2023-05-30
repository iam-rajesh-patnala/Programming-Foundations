def get_ordered_string(word_1, word_2, word_3, order):
    result = ""
    for num in order:
        if num == "1":
            result += word_1
        elif num == "2":
            result += word_2
        elif num == "3":
            result += word_3
    print(result)



def root():
    word_1, word_2, word_3 = input(), input(), input()
    order = input()
    get_ordered_string(word_1, word_2, word_3, order)
root()


# ----------------------------------------


def get_concatinated_word(words, t):
    concatinated_word = ""
    for each_number in t:
        index = int(each_number) - 1
        concatinated_word += words[index]
    return concatinated_word

def read_words(no_of_inputs):
    words = []
    for i in range(no_of_inputs):
        word = input()
        words.append(word)
    return words

def main():
    words = read_words(3)
    t = input()
    concatinated_word = get_concatinated_word(words, t)
    print(concatinated_word)
    
main()