def get_triplets(S, T):
    count = 0
    for i in range(S+1):
        for j in range(S+1):
            for k in range(S+1):
                if (i + j + k <= S) and (i * j * k <= T):
                    count += 1
    print(count)




def root():
    S, T = map(int, input().split())
    get_triplets(S, T)
root()