a = input()
len_of_a = len(a)
b = a[0]
for i in range(1, len_of_a):
    b = b + "-" + a[i]
print(b)
