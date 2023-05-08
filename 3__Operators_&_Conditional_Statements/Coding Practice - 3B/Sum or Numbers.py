num_1 = int(input())
num_2 = int(input())


if num_1 < 20 or num_2 < 20 or (30 < (num_1 + num_2) < 50) :
    print(num_1 + num_2)
else:
    print(num_1, num_2, sep="\n")