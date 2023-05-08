def find_mean(num_list):
    length = len(num_list)
    total = 0
    for num in num_list:
        total += num
    avg = total / length
    print("Mean: " + str(round(avg, 2)))


def find_median(num_list):
    length = len(num_list)
    sorted_list = sorted(num_list)  # ------  num_list.sort() ------ this is also sorted
    if length % 2 == 0:
        m1 = num_list[length // 2]
        m2 = num_list[length // 2 - 1]
        m = (m1 + m2) / 2
    else:
        m = num_list[length // 2]
    print("Median: " + str(round(m, 2)))


def find_mode(num_list):
    pass


num_list = list(map(int, input().split()))
find_mean(num_list)
find_median(num_list)
find_mode(num_list)
