num = int(input())
max_final_list = []
for i in range(num):
    update_list = input().split()
    conv_int_list = list(map(int, update_list))
    max_final_list.append(max(conv_int_list))
print(max_final_list)
