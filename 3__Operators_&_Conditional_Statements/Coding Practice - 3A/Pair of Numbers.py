num_1 = int(input())
num_2 = int(input())

both_less = num_2 <= 1000 and num_1 <= 1000
num_2_grater = num_2 > 500

if both_less or num_2_grater:
    print("Pair")
else:
    print("Not a Pair")
