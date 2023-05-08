num = int(input())


last = ""
for i in range(1, num+1):
    
    if i == 1 or i == num:
        result = ""
        for j in range(num):
            result += str(num-j) + " "
            last = str(num-j)
        print(result)
    else:
        hallow_spaces = "  "
        result = str(num) + " " + hallow_spaces*(num-2) + last
        print(result)