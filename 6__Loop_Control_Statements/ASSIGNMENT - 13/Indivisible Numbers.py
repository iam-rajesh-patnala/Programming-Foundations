num = int(input())  # 11
count = 0

for i in range(1, num + 1):
    is_divisible = "True"
    for j in range(2, 11):
        if i % j == 0:
            is_divisible = "False"
            break
    if is_divisible == "True":
        count += 1
print(count)    # 2
