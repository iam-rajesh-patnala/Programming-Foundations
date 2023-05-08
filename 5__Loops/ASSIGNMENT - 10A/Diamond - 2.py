num = int(input())

space = " "

for i in range(1, num * 2):
    if i <= num:
        result = space * (num - i) + (str(i) + " ") * i
        print(result)
    else:
        result = space * (i - num) + (str(num*2 - i) + " ") * (num*2 - i)
        print(result)
