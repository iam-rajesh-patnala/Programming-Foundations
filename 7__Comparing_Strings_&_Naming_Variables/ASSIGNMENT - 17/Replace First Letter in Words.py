word = input().split()
new = ""
for char in word:
    new += chr(ord(char[0]) + 1) + char[1:] + " "

print(new)
