num = int(input())
starter = 5
count = 0

for i in range(1, num + 1):
    left_spaces = " " * (num - i)
    hallow_space = " "
    result = ""
    if i == 1:
        result = left_spaces + str(starter)
        print(result)
    elif i == num:
        for j in range(num):
            result += str(starter + j) + " "
        print(result)
    else:
        val = num - 1 + i
        result = left_spaces + str(starter) + " " + hallow_space * count + str(starter - 1 + i)
        count += 2
        print(result)
