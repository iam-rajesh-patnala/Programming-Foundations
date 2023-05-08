num_list = list(map(int, input().split()))
length = len(num_list)

total_sum = 0

for i in range(length):
    for j in range(i, length):
        result = num_list[i : j + 1]
        total = sum(result)
        if total > total_sum:
            total_sum = total
print(total_sum)
