num = int(input())
num2 = int(input())

total_list = []

for i in range(num):
    seq = int(input())
    total_list += [seq]
for j in range(num2):
    op = int(input())
    output = total_list[op]
    print(output)
