num = int(input())

total_list =[]
count = 0
length = len(total_list)

for i in range(num):
    word = input()
    total_list+= [word]
    count+= 1
#print(count)
for j in range(1,num+1):
    vin = count - j
    print(total_list[vin])