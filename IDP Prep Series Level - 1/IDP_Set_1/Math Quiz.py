def get_sum(start_range, end_range, number_seq):
    sum = 0
    for num in number_seq:
        if num >= start_range and num <= end_range:
            sum += num
    return sum
def seq(next_series, number_series):
    for i in range(next_series):
        start_range, end_range = map(int, input().split())
        sum_of_numbers = get_sum(start_range, end_range, number_series)
        print(sum_of_numbers)

def root():
    number_series = list(map(int, input().split()))
    next_series = int(input())
    seq(next_series, number_series)


root()