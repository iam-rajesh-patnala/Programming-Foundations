num = int(input())

space = "  "
star = "* "

for i in range(1, num*2 +1):
    if i <= num:
        center_spaces = space * (num - i)
        result = star*i + center_spaces*2 + star*i
        print (result)
    else:
        center_spaces = space * (i - num)
        result = star* (num*2 - i) + center_spaces*2 + star* (num*2 - i)
        print (result)