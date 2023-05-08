sentence = input().split()
# L, K = input().split()
# L, K = int(L), int(K)

L, K = [int(i) for i in input().split()]



result = []

for i in sentence:
    if len(i) > L:
        A = K % len(i)
        print(A)
        part = i[-A:]
        remaining = i[:-A]
        full = part + remaining
        result.append(full)
    else:
        result.append(i)


print(*result, sep = " ")
