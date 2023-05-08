num_1 = int(input())
num_2 = int(input())

less_than_60 = (num_1 < 60) or (num_2 < 60)
grater_than_80 = (num_1 > 80) or (num_2 > 80)

if less_than_60 and grater_than_80:
    print(True)
else:
    print(False)
