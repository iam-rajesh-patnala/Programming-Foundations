num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


val_1 = True
val_2 = True
val_3 = True


if num_1 < 20:
    val_1 = False
elif num_2 < 20:
    val_2 = False
elif num_3 < 20:
    val_3 = False

True_value = val_1 and val_2 and val_3
False_value = False

if True_value:
    print(True_value)
else:
    print(False_value)
