num = int(input())


space = " "

for i in range(num):
    result = space*i + str(num-i)* (num-i)
    print(result)
