num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

n1_n2 = (num_1 + num_2) > 10
n2_n3 = (num_2 + num_3) > 10
n3_n1 = (num_3 + num_1) > 10

if n1_n2 and n2_n3 and n3_n1:
    print(True)
else:
    print(False)
