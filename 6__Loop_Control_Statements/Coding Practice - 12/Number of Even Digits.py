num = int(input())

even =  0
for digit in str(num):
    if int(digit) % 2 == 0:
        even+= 1


if even > 2:
    print("Count of even digits is greater than two")
else:
    print("Count of even digits is not greater than two")
