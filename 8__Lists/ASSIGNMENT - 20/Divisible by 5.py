num = int(input())

list_a = list()

for i in range(num):
    num2 = int(input())
    if num2 % 5 == 0:
        list_a.append(num2)
    
print(list_a)