num = int(input())
num2 = input()
split_num2 = num2.split()
length = len(split_num2)

total_list = []

if (num % 2) == 0:
    val = int(num / 2)
    for i in range(0, val):
        total_list += [int(split_num2[-val + i])]
    print(total_list)
elif (num % 2) == 1:
    val = int(num / 2)
    for i in range(0, val):
        total_list += [int(split_num2[-val + i])]
    print(total_list)
