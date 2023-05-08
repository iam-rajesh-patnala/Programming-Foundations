word = input().split() # This is my favorite cookie
num = int(input())     # 4

new = []

for char in word:
    new = [char] + new

print(new[:num]) # ['cookie', 'favorite', 'my', 'is']

word = None