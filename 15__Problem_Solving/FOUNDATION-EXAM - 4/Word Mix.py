words = input().split()
list_a = []

for word in words:
    for i in range(len(word)):
        if (len(list_a) > i):
            list_a[i] += word[i]
        else:
            list_a.append(word[i])


print(*list_a, sep = ' ')
