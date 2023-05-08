num = int(input())

star = "* "
space = " "

for i in range(1, num + 1):
    result = space* (num-i) + star*i
    print(result)