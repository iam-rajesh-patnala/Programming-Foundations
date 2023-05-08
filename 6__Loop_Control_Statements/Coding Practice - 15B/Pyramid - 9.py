num = int(input())  # 5

zero = "0 "
dot = ". "
count = 1

for i in range(1, num + 1):
    print(dot * (num - i) + zero * count + (dot * (num - i)))
    count = count + 2
    # . . . . 0 . . . . 
    # . . . 0 0 0 . . . 
    # . . 0 0 0 0 0 . . 
    # . 0 0 0 0 0 0 0 . 
    # 0 0 0 0 0 0 0 0 0