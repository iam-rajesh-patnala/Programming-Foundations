num = int(input())

count = 0

for digit in str(num):
    if digit == "0":
        count += 1
    
    
if count > 3:
    print("Count of zeroes is greater than three")
else:
    print("Count of zeroes is not greater than three")

