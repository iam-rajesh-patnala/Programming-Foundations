num = int(input())

count = 1

for i in range(1, num*2):
    if i == 1 or i == num*2-1:
        left_spaces = " " * (num - 1)
        val = left_spaces + chr(64 + 1)
        count += 1
        print(val)
    elif i <= num:
        left_spaces = " " * (num - i)
        hollow_spaces = " " * (count - 2)
        first_alpha = chr(64 + count)
        second_alpha = chr(ord(first_alpha) + 1)
        val = left_spaces + first_alpha + " " + hollow_spaces + second_alpha + " "
        count += 2
        print(val)
    else:
        left_spaces = " " * (i - num)
        hollow_spaces = " " * (count - 6)
        first_alpha = chr(64 + count-4)
        second_alpha = chr(ord(first_alpha)+1 )
        val = left_spaces + first_alpha + " " + hollow_spaces + second_alpha + " "
        count -= 2
        print(val)