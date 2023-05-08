nums = sorted(list(map(int, input().split(","))))

if len(nums) % 2 == 0:
    val = nums[len(nums) // 2 -1] + nums[len(nums) // 2]
    print(val / 2)

else:
    val = nums[len(nums) // 2]
    print(val)

