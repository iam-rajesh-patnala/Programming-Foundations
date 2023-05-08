num = input()
length = len(num)
int_num = int(num)

sum = 0
# val = 0

for i in range(length):
    single_digit = num[i]
    # val = val + 1
    cube = int(single_digit) ** length
    sum = sum + cube
if sum == int_num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
