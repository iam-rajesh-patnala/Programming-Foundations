def list_items(list_num):
    # 1st method----------
    # total = []
    # for i in range(0, len(list_num)):
    #     total +=[int(list_num[i])]

    # 2nd method----------
    # for i in range(0, len(list_num)):
    #     list_num[i] = int(list_num[i])

    # 3rd method----------
    # res = [eval(i) for i in list_num]

    # 4th method----------
    # list_num = [int(i) for i in list_num]

    # float val & int val conversion--------
    # lis = ['1.1', '4', '3.5', '6.7', '7.2']
    # res = [round(float(i)) for i in lis]

    max_num = max(map(int, list_num))
    print(max_num)


list_num = input().split(",")
list_items(list_num)
