num = int(input())

loop = int(input())

counter = 0
for i in range(1, loop + 1):
    result = ""
    if i == 1 or i == loop:
        for j in range(loop):
            val = num + j
            result += str(val) + " "
            counter = val
        print(result)

    else:
        hollow_space = "  "
        hollow_space_count = loop - 2
        val = counter + 1
        next_val = val + hollow_space_count + 1
        result = str(val) + " " + hollow_space * (hollow_space_count) + str(next_val)
        counter = next_val
        num = next_val + 1
        print(result)
