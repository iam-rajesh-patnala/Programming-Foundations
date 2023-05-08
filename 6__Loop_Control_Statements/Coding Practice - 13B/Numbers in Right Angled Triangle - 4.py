starting_digit = int(input())
loop_count = int(input())

count = starting_digit

for i in range(1, loop_count+1):
    result = ""
    for j in range(i*2):
        result += str(count) + " "
        count += 1
    print (result)