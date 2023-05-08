num = int(input())

for i in range (1, num*2):
    if i <= num:
        result = "* " * i
        print(result)
    else:
        result = "* " * (num*2 - i)
        print(result)