num_list = list(map(int, input().split()))

'''
smallest = num_list[0]
for num in num_list:
    if num < smallest:
        smallest = num
'''


smallest = min(num_list)

print(smallest)