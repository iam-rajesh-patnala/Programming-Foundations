num = int(input())

plus = "+ "
star = "* "
spaces = " "

for i in range(num):
    if i == 0:
        result = spaces * (i) + plus * (num - i)
        print(result)
    else:
        result = spaces * (i) + star * (num - i)
        print(result)