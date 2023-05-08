word = input().split()


for char in word:
    if char[0].lower() == char[-1].lower():
        print(True)
    else:
        print(False)