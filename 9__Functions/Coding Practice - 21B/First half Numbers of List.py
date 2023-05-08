num_list = list(map(int, input().split()))

if len(num_list) % 2 == 1:
    print(num_list[:(len(num_list) + 1)//2])
else:
    print(num_list[:len(num_list)//2])