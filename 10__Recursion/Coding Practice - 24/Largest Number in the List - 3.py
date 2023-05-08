def find_largest_num(nums):
    return max(nums)


nums = list(map(int, input().split(",")))
index = int(input())  # 10,7,2,5

print(find_largest_num(nums[index:]))  # 7
