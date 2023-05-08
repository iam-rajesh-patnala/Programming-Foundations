def largest(arg_1, arg_2):
    arg_1 = list(map(int, arg_1))
    arg_1.sort()
    count = -1
    print(str(arg_1[arg_2 + count]))


num_list = input().split(",")
index = int(input())
largest(arg_1=num_list, arg_2=index)
