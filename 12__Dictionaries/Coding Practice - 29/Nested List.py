num = int(input())
final_list = []
for i in range(num):
    update_list = input().split()
    conv_int_list = list(map(int, update_list))
    final_list.append(conv_int_list)
print(final_list)
