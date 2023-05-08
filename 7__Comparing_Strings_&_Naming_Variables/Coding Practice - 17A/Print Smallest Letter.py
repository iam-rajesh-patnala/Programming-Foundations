string = input()

smallest_character = string[0]

for index in range(1, len(string)):
    if ord(string[index]) < ord(smallest_character):
        smallest_character = string[index]

print(smallest_character)


#----------------------------------

word = input()

main = []
for i in range(len(word)):
    main.append(ord(word[i]))
    

m = min(main)

print(chr(m))