def get_sum_of_series(number, number_of_terms):
    # Complete this recursive function
    total = 0
    if number_of_terms == 0:
        return number_of_terms
    total += number + get_sum_of_series(number - 2, number_of_terms - 1)
    return total


number = int(input())
number_of_terms = int(input())

series_sum = get_sum_of_series(number, number_of_terms)  # Call the get_sum_of_series function
print(series_sum)
