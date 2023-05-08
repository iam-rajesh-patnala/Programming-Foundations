num_1 = int(input())
num_2 = int(input())

is_positive = (num_1 > 0) and (num_2 > 0)
is_less_70 = (num_1 < 70) and (num_2 < 70)

if is_positive or is_less_70:
    print(True)
else:
    print(False)
