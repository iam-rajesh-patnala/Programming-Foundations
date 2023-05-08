num = int(input())

total_list = []

for i in range(num):
    list_items = input()
    total_list += [list_items]
    
    
first_three_objects = total_list[:3]
last_three_objects = total_list[num-3:]
print(first_three_objects+last_three_objects)
