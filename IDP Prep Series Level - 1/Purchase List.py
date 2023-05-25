def max_purchase(purchases):
    high = None
    for num in purchases:
        if purchases.count(num) > 1:
            high = num
            break

    return high

def min_purchase(purchases):
    low = None
    for num in purchases:
        if purchases.count(num) == 1:
            low = num
            break
    return low



purchases = list(map(int, input().split()))

minimum, maximum = min_purchase(purchases), max_purchase(purchases)
print(minimum, maximum, sep="\n")