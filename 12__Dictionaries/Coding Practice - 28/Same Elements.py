num = input().split()
int_num = list(map(int, num))
set_ele = set(int_num)

length = len(set_ele)

if length == 1:
    print("True")
else:
    list_conv = list(set_ele)
    list_conv.sort()
    print(list_conv)
    # print(sorted(list(set_ele)))
