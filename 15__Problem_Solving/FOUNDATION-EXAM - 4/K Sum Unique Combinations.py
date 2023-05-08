from itertools import combinations

numbers = list(map(int, input().split))
numbers.sort()
total_number = int(input())

length = len(numbers)
count = 0

for i in range(1, length+1):
    combi = list(set(combinations(numbers, i)))
    #print(combi)
    for num in combi:
        if sum(num) == total_number:
            #print(sum)
            count += 1

print(count)
