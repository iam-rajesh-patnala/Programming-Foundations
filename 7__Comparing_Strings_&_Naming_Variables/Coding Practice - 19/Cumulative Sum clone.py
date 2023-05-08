num = int(input())
# 5
# 8
# 11
# -96
# 49
# 85

count = 0

for i in range(1, num + 1):
    seq_num = int(input())
    for j in range(1):
        count = seq_num + count
    print(count)
    # 8
    # 19
    # -77
    # -28
    # 57