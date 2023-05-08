num = int(input())  # 5

count = 0
for i in range(1, num + 1):
    lr_dots_count = num - i
    lr_dots = ". " * lr_dots_count
    zero_count = count + i
    count += 1
    zero = "0 " * zero_count
    print(lr_dots + zero + lr_dots)

count = -3
for j in range(1, num):
    lr_dots_count = j
    lr_dots = ". " * lr_dots_count
    zero_count = num * 2 + count
    count -= 2
    zero = "0 " * zero_count
    print(lr_dots + zero + lr_dots)
    # . . . . 0 . . . . 
    # . . . 0 0 0 . . . 
    # . . 0 0 0 0 0 . . 
    # . 0 0 0 0 0 0 0 . 
    # 0 0 0 0 0 0 0 0 0 
    # . 0 0 0 0 0 0 0 . 
    # . . 0 0 0 0 0 . . 
    # . . . 0 0 0 . . . 
    # . . . . 0 . . . .