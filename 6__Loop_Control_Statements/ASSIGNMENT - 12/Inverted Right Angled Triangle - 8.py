num = int(input())

spaces = "  "
star = "* "
count = 1
for i in range(1, num+1):
    left_spaces = spaces * (count - 1)
    result = left_spaces + ((num*2)-count) * star
    count+= 2
    print(result)