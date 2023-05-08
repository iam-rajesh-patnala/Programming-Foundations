number = int(input())  # 12
k = int(input())  # 3
factor = number
count = 0
kth_factor_found = False


for i in range(1, number + 1):
    if not kth_factor_found:
        if (number % factor) == 0:
            count = count + 1
        if count == k:
            print(factor)  # 4
            kth_factor_found = True
        elif factor < k:
            print("1")
            break
    factor = factor - 1
