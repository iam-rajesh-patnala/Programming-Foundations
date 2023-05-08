num = int(input())

count = -1
for i in range(1, num+1):
    left_spaces = num - i
    left_space = " "*left_spaces
    hollow_spaces = count + i
    count+= 1
    hollow_space = " "*hollow_spaces
    row_output = (left_space + "/" + hollow_space + "\\")
    print(row_output)
    

for j in range(0, num):
    left_spaces = j
    left_space = " "*left_spaces
    hollow_spaces = count*2
    count-= 1
    hollow_space = " "*hollow_spaces
    row_output = (left_space +"\\" + hollow_space + "/")
    print(row_output)