nums = sorted(list(map(int, input().split(","))), reverse=True)  # 1,9,3,1,2,7,4,8
index = int(input())  # 2
val = min(nums[index:])

print(val)  # 1
