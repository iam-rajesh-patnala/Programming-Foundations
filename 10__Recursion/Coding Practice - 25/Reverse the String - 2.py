def get_reversed_string(string):
    # Complete this recursive function
    each_word = string[0]
    if len(string) <= 1:
        return each_word
    return get_reversed_string(string[1:]) + each_word


string = input() # react

resultant_string = get_reversed_string(string)  # Call the get_reversed_string function
print(resultant_string)     # tcaer


# simple form
"""
word = input()

print(word[::-1])
"""