def smallest(num_list):
    num_list = min(map(int, num_list))
    print(num_list)


num_list = input().split(",")
smallest(num_list)
