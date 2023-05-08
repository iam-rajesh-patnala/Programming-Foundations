num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

case_1 = (num_1 + num_2) > num_3
case_2 = (num_2 + num_3) > num_1
case_3 = (num_3 + num_1) > num_2

if case_1 and case_2 and case_3:
    print(True)
else:
    print(False)
