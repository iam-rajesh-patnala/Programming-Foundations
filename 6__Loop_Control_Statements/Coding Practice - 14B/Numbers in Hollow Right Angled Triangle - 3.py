num = int(input())
rows = int(input())

counter = 0

for i in range(1, rows+1):
    result = ""
    if i == 1:
        first_row = str(num) + " "
        print(first_row)

    elif i == rows:
        for j in range(1, rows+1):
            result += str(counter + j) + " "
        print(result) 
    else:
        each_row = str(num+i)+" "
        hollow_space = "  " * (counter - i  +1)
        each_row += hollow_space
        counter += 1
        each_row += str(num+counter+1)
        print(each_row)
