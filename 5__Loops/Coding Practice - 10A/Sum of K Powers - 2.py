num = input()

length = len(num)

result = 0

for char in num:
    result+= int(char)**length


print(result)