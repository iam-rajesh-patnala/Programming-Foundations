word = input().split()

new = []
for char in word:
    new += char[2]

print(*new, sep=",")

'''
word = input().split()

new = []

for char in word:
    if len(char) > 2:
        new += char[2]
        
print(",".join(new))
        
'''

