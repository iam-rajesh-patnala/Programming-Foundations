num = int(input())


for i in range(1, num + 1):
    length = len(str(i))
    result = 0
    for digit in str(i):
        result += int(digit) ** length

    if result == i:
        print(i)