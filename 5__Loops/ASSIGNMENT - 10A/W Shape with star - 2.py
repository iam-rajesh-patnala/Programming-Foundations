num = int(input())

star = "* "
space = " "
hollow = "  "
for i in range(0, num):
    if i > 1:
        s = space * i
        d = star * (num - i)
        king = s + d
        h = hollow * (i - 1)
        print(king + h + d)
    else:
        r = (i) * space + star * ((num * 2 - i - 1))
        print(r)
