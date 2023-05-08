rows = int(input()) 
columns = int(input())

number = 1

for row in range(1, rows+1):
    
    if row == 1 or row == rows:
        each_row = ""

        for column in range(1, columns + 1):
            each_row = each_row + (str(number) + " ")
            number = number + 1
        
        print(each_row)
    else:
        
        each_row = (str(number) + " ")
        hollow_spaces = "  " * (columns - 2)
        
        number = number + int(len(hollow_spaces) / 2) + 1
        each_row = each_row + hollow_spaces + (str(number) + " ")
        
        number = number + 1
        
        print(each_row)