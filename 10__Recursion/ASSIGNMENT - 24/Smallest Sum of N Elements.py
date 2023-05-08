number_list = sorted(list(map(int, input().split(",")))) # 2,10,9,6,5
index = int(input())

smallest_sum = sum(number_list[:index])

print(smallest_sum) # 3