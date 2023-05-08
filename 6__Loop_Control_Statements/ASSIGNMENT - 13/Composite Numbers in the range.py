num1 = int(input())  # 2
num2 = int(input())  # 9

for i in range(num1, num2 + 1):
    count = 0
    for j in range(2, i + 1):
        if i % j == 0:
            count += 1
    if count >= 2:
        print(i)
        # 4
        # 6
        # 8
        # 9
