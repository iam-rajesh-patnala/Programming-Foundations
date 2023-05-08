word = input()

for i in range(len(word)):
    result = word[:len(word)-i]
    print(result)