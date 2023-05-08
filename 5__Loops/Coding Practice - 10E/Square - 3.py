num = int(input())

star = "* "
zero = "0 "

for i in range(1, num+1):
    if i == 1 or i == num:
        result = star * num
        print(result)
    else:
        result = star + zero*(num - 2) + star
        print(result)