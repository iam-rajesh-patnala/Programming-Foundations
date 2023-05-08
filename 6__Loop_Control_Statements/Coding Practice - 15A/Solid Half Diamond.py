n = int(input())  # 5

var = ""


for i in range(0, n):
    star = "* "
    var = var + star
    print(var)

for j in range(1, n):
    star2 = "* "
    var = star2 * (n - j)
    print(var)
    # *
    # * *
    # * * *
    # * * * *
    # * * * * *
    # * * * *
    # * * *
    # * *
    # *
