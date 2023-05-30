def check_words_equal(word1, word2):
    if (word1 == word2):
        return "Yes"
    else:
        return "No"

def swap(first_input, second_input):
    first_input_list = list(first_input)
    second_input_list = list(second_input)
    for i in range(len(first_input_list) - 1):
        if first_input_list[i] != second_input_list[i]:
            flag = first_input_list[i]
            first_input_list[i] = first_input_list[i+1]
            first_input_list[i+1] = flag
            break
    equal = check_words_equal(first_input_list, second_input_list)
    return equal


def first_case():
    first_input = input()
    second_input = input()
    result = swap(first_input, second_input)
    print(result)

first_case()

# ------------------------------------

# def check_words_for_equality(first_word_list, second_word_list):
#     if first_word_list == second_word_list:
#         return "Yes"
#     else:
#         return "No"


# def swap_characters_and_check_words_equality(first_word, second_word):
#     first_word_list, second_word_list = list(first_word), list(second_word)
#     for i in range(len(first_word_list) - 1):
#         if first_word_list[i] != second_word_list[i]:
#             temp = first_word_list[i]
#             first_word_list[i] = first_word_list[i + 1]
#             first_word_list[i + 1] = temp
#             break
#     are_words_equal = check_words_for_equality(first_word_list, second_word_list)
#     return are_words_equal


# def main():
#     first_word, second_word = input(), input()
#     result = swap_characters_and_check_words_equality(first_word, second_word)
#     print(result)


# main()
