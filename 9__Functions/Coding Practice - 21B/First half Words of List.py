word = input().split()


if len(word) % 2 == 1:
    print(word[:(len(word)+1) // 2])
else:
    print(word[:len(word) // 2])