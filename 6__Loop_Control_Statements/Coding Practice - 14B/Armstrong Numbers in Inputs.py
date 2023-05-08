num = int(input())

list_a = []
for i in range(num):
    list_a.append(int(input()))


for num2 in list_a:
    total = 0
    length = len(str(num2))

    for j in range(length):
        total += int(str(num2)[j]) ** length
    if total == num2:
        print(num2)
