num = int(input())

starting_count = 0
space = "  "
for nums in range(1, num + 1):
    starting_count += nums


for i in range(num):
    result = ""
    left_space = (i) * space
    for j in range(num - i):
        result += str(starting_count) + " "
        starting_count -= 1
    output = left_space + result
    print(output)
