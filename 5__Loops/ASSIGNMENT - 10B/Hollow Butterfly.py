num = int(input())

star = "* "
space = "  "

count = 0
for i in range(1, num*2+1):
    if i == 1 or i == num*2:
        center_space = space * (num*2-2)
        result = star + center_space + star
        print(result)
    elif i <= num:
        center_space = space * (num*2- i*2)
        hallow_space = space * (i-2)
        count += 1
        result = star + hallow_space + star + center_space + star  + hallow_space + star
        print(result)
    else:
        center_space = space * (i*2 - num*2-2)
        hallow_space = space * (count-1)
        count -= 1
        result = star + hallow_space + star + center_space + star  + hallow_space + star
        print(result)




    
