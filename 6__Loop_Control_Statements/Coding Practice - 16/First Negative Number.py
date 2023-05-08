r = int(input())

neg = False

for num in range(r):
    s = int(input())
    if not (s >= 0):
        neg = True
        break
if neg:
    print(s)
else:
    print("No Negative Numbers")
    