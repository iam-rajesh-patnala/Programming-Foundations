num = int(input())

limit = 0
for nums in range(num, 0, -1):
    limit += nums
    
next_count = 0

for i in range(1, num+1):
    hollow_space = "  "
    result = ""
    if i == 1:
        for j in range(1, num+1):
            result += str(j) + " "
            next_count = j
        print(result)
    elif i == num:
        result = str(limit) + " "
        print(result)
    else:
        hollow_space_count = num-i
        result = str(next_count) + " " + (hollow_space * (hollow_space_count-1)) + str(hollow_space_count+next_count) + " "
        next_count = hollow_space_count+next_count
        print(result)
    next_count += 1
