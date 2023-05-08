num = int(input())  # 5

number = "1 "
gong = ""
for i in range(1, num + 1):
    sam = "0 " * (num - i) + (number + gong) + "0 " * (num - i)
    gong = gong + 2 * ("1 ")
    print(sam)
    # 0 0 0 0 1 0 0 0 0 
    # 0 0 0 1 1 1 0 0 0 
    # 0 0 1 1 1 1 1 0 0 
    # 0 1 1 1 1 1 1 1 0 
    # 1 1 1 1 1 1 1 1 1 