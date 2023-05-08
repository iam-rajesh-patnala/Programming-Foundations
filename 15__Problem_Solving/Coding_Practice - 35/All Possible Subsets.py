from itertools import combinations

sentence = sorted(input().split())
length = len(sentence)

for i in range(1, length+1):
    combi = combinations(sentence, i)
    combi = list(set(combi))
    for j in sorted(combi):
        print(*j)