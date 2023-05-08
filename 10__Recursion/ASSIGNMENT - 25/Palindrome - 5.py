def is_palindrome(string):
    # Complete this recursive function
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and is_palindrome(string[1:-1])




string = input()    # Noon

is_true = is_palindrome(string.lower())  # Call the is_palindrome function

print(is_true)  # True