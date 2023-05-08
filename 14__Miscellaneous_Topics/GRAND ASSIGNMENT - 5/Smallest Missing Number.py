nums = list(map(int, input().split()))

lists = 1

for i in range(len(nums)):
    if lists in nums:
        lists += 1
    else:
        print(lists)
        break
