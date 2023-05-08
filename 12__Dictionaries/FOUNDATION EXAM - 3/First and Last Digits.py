num_1 = int(input())
num_2 = int(input())

counter = 0

for i in range(num_1, num_2 + 1):
    i = str(i)
    if len(i) == 1:
        counter += 1
    else:
        first = i[0]
        last = i[1]
        if first == last:
            counter += 1

print(counter)
