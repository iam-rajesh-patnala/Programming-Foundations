n = int(input())  # 10
k = int(input())  # 5
m = n
for num in range(k):
    m = m + num
res = n + (k * (k + 1)) // 2 - 1
for i in range(k):
    pattern = ""
    for j in range(i + 1):
        pattern = pattern + (str(res) + " ")
        res = res - 1
    print(pattern)
    # 24
    # 23 22
    # 21 20 19
    # 18 17 16 15
    # 14 13 12 11 10
