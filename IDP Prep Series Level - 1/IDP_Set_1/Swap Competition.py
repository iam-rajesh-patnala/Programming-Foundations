def get_swap_result(first_word, second_word):
    condition = True
    length = len(first_word) == len(second_word)
    first_word = list(first_word)
    if length:
        for char in second_word:
            if char not in first_word:
                condition = False
    if length and condition:
        return "YES"
    else:
        return "NO"

def root():
    result = []
    loop = int(input())
    for i in range(loop):
        first_word, second_word = input().split()
        result.append( get_swap_result(first_word, second_word))
    print(" ".join(result))
root()



"""def check_for_rearrangement_of_letters(first_word, second_word):
    if len(first_word) != len(second_word):
        return "NO"
    is_rearrangement_possible = "YES"
    for each_letter in first_word:
        if (first_word.count(each_letter) != second_word.count(each_letter)):
            is_rearrangement_possible = "NO"
            break
    return is_rearrangement_possible
    
def main():
    test_cases = int(input())
    result = ""
    for i in range(test_cases):
        first_word, second_word = input().split()
        is_rearrangement_possible = check_for_rearrangement_of_letters(first_word, second_word)
        result += is_rearrangement_possible + " "
    print(result)
    
main()"""