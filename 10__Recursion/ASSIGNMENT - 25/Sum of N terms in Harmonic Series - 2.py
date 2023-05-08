def get_series_sum(number):
    # Complete this recursive function
    if number <= 1:
        return number
    return 1 / number + get_series_sum(number - 1)


number = int(input())

series_sum = get_series_sum(number)
val = round(series_sum, 2)
print(val)
