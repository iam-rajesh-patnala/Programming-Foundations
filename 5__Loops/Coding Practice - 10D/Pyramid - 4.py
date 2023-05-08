num = int(input())

space = " "

for i in range(1, num*2):
    if i <= num:
        result = (str(i)+ space) * i
        print(result)
    else:
        result = ((str(num*2 - i)) + space) * ((num*2) - i)
        print(result)