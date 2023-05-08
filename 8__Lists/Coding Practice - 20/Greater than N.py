num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]
# Write your code here
num = int(input())
length = len(num_list)
total =[]
for i in range(length):
    if num_list[i] > num:
        total += [num_list[i]]
print(total)