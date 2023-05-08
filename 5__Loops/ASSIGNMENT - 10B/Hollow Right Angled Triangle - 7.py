num = int(input())

plus = '+ '
star = '* '

for i in range(1, num+1):
    if i == 1:
        print(plus * num)
    elif i <= num-1 :
        left_space = '  ' * (i-1)
        hallow_space = '  ' * (num-1 -i)
        result = left_space + star + hallow_space + star
        print(result)
    else:
        left_space = '  ' * (i-1)
        print(left_space + "* ")