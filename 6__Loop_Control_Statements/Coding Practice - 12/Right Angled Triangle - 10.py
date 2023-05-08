num = int(input())

star = "* "

count = 1
for i in range(num):
    result = (count) * (star)
    count += 2
    print(result)
