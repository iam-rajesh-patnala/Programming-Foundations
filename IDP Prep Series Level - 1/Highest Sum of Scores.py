def get_highest_sum(num_series):
    return sum(num_series)

def root():
    num = int(input())
    sum = 0
    output = ""
    for i in range(num):
        num_series = list(map(int, input().split(",")))
        result = get_highest_sum(num_series)
        if result > sum:
            output = num_series
            sum = result
    print(*output)


root()