num = int(input())

star = "* "

for i in range(1, num+1):
    left_space = " " * (num - i)


    if i == 1 or i == num:
        result = (left_space) + star * i 
        print(result)
    else:
        hallow_space_count = i -2
        hallow_space = hallow_space_count * "  "
        result = left_space + star + hallow_space + star
        print(result)