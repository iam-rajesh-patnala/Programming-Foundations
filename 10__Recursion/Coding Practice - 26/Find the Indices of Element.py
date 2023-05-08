list_a = [5, 4, 10, 2, 3, 2, 5, 15, 4, 4]
# write your code here
index = int(input())

length = len(list_a)

total = []
for i in range(length):
    if list_a[i] == index:
        total.append(i)



print(*total)