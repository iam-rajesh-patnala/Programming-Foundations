num = int(input())

count = ""
for i in range(1, num + 1):
    first = ""
    for j in range(1, i + 1):
        first += str(j) + " "
    result = first + count
    count = first
    print(result)
