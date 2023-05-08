num_1 = int(input())
num_2 = int(input())

sum = num_1 + num_2
product = num_1 * num_2

if (len(str(sum)) < 3) and (len(str(product)) < 3):
    print(True)
else:
    print(False)
