for_loop = int(input())
num = int(input())

sum = 0

for i in range(1, num+1):
    sum+= i

starting = sum + for_loop -1



for i in range(1, num+1):
    result = ""
    for j in range(i):
        result += str(starting) + " "
        starting -= 1
    print (result)

