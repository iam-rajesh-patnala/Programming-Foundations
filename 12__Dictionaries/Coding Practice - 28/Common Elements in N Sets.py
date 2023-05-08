def fun(list_all):
    res = list_all[0]
    for num in list_all:
        res = res.intersection(num)
    return res


num = int(input())
list_all = []

for i in range(1, num + 1):
    set_1 = input().split()
    set_1 = set(map(int, set_1))
    list_all.append(set_1)

result = fun(list_all)
list_conv = list(sorted(result))
print(list_conv)
