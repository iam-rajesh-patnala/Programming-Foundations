num1 = int(input())  # 150
num2 = int(input())  # 153
count = 0

for i in range(num1, num2 + 1):
    i = str(i)
    length = len(i)
    total = 0
    for j in range(length):
        index = i[j]
        total = total + (int(index) ** length)
    if str(total) == i:
        count += 1
        print(total, end=" ")  # 153

if count == 0:
    print("-1")
