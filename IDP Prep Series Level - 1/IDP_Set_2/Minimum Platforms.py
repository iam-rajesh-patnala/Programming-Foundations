def get_no_platforms_needed(arrival, departure, no_of_trains):
    arrival.sort()
    departure.sort()

    platforms_needed = 1
    max_platforms_needed = 1

    i = 1
    j = 0

    while i < no_of_trains and j < no_of_trains:
        if arrival[i] <= departure[j]:
            platforms_needed += 1
            i += 1
        else:
            platforms_needed -= 1
            j += 1
        if platforms_needed > max_platforms_needed:
            max_platforms_needed = platforms_needed

    return max_platforms_needed


def root():
    arrival = list(input().split())    #  0900 0940 0950 1100 1500
    departure = list(input().split())  #  0910 1200 1120 1130 1900
    no_of_trains = len(arrival)
    result = get_no_platforms_needed(arrival, departure, no_of_trains)
    print(result)   # 3


root()
