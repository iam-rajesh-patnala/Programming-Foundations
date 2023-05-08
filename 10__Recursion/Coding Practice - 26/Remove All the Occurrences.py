nums_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100]

num = int(input())
length = len(nums_list)

for j in range(len(nums_list)):
    for i in nums_list:
        if i == num:
            nums_list.remove(num)
            break

print(nums_list)
