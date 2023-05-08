num = int(input())


spaces = "  "
star = "* "

for i in range(1, num+1):
    if i == 1:
        center_space = spaces * (num*2 - (i+1))
        result = star + center_space + star
        print(result)

    elif i <= num -1:
        center_space = spaces * (num*2 - (i*2))
        hallow_space = spaces * (i-2)
        star_hollow = star + hallow_space + star
        result = star_hollow + center_space + star_hollow
        print(result)
    
    else:
        result = star * (num*2)
        print(result)
