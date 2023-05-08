word = input()
length = len(word)
fw = ""

for i in range(length):
    num = int(input())
    fw = fw + word[num]
print(fw)
