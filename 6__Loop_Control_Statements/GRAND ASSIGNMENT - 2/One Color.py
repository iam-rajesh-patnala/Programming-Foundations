word = input()

g_count = 0
r_count = 0


for char in word:
    if char == "G":
        g_count += 1
    else:
        r_count += 1
if g_count > r_count:
    print(r_count)
else:
    print(g_count)
