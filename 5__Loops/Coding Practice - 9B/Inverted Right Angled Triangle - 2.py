num = int(input())

for i in range(num+1):
    result= (str(num-i) + " ") * (num-i)
    print(result)