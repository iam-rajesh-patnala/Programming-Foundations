def get_diff(heights):
    min_list = []
    for i in range(len(heights)):
        key = heights[i]
        for num in heights[i + 1 :]:
            min_list.append(key - num)

    print(min(min_list))


def root():
    heights = list(map(int, input().split()))
    heights = sorted(heights, reverse=True)
    get_diff(heights)


root()


# ---------------------------------------

def get_min_absolute_difference(pyramid_heights):
    min_absolute_difference = abs(pyramid_heights[1] - pyramid_heights[0])
    for i in range(len(pyramid_heights)):
        for j in range(i + 1, len(pyramid_heights)):
            difference = abs(pyramid_heights[i] - pyramid_heights[j])
            if(difference < min_absolute_difference):
                min_absolute_difference = difference
    return min_absolute_difference

def main():
    pyramid_heights = list(map(int,input().split()))
    min_absolute_difference = get_min_absolute_difference(pyramid_heights)
    print(min_absolute_difference)

main()