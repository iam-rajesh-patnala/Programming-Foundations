num_1 = int(input())
num_2 = int(input())

grater = num_1 > 300 or num_2 > 300
sum = num_1 + num_2 < 500

if grater and sum:
    print("Can team up")
else:
    print("Cannot team up")
