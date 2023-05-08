def count_of_uppercase(word):
    count = 0
    for char in word:
        if char.isupper():
            count += 1
    return count
    # complete this function



word = input()

result = count_of_uppercase(word)# Call the count_of_uppercase function

print(result)