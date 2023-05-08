num = int(input())

dot = ". "
zero = "0 "

for i in range(1, num+1):
    if i <= 2 or i == num:
        result = dot * i 
        print(result)
    else:
        result = dot + zero * (i-2) + dot
        print(result)