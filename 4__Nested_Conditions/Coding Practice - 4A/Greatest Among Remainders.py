N = int(input())

val_1 = N % 4
val_2 = N % 5

if val_1 >= val_2:
    print(val_1)
else:
    print(val_2)
