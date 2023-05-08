num = int(input())

count = 0

for i in range(1, num * 2):
    result = ""
    if i == 1 or i == num * 2 - 1:
        res = " " * (num-1) + "1 "
        print(res)
    elif i <= num:
        left_spaces = " " * (num - i)
        space = " " * (count)
        result = left_spaces + "1 " + space + str(i)
        count+= 2
        print(result)
    else:
        left_spaces = " " * (i - num)
        space = " " * (count-4)
        result = left_spaces + "1 " + space + str(num*2 - i)
        count -= 2
        print(result)