def get_series_sum(number):
    # total = 0
    # for i in range(1, number+1):
    #     total += 1/i
    # return round(total, 2)
    if number <= 1:
        return number
    
    val = round(1/number + get_series_sum(number-1), 2)
    return val






number = int(input())

series_sum = get_series_sum(number)

print(series_sum)

# print(round(1+1/2+1/3, 2) )