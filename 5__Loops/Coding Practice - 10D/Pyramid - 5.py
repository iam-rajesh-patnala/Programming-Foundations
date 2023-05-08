num = int(input())

spaces = "  "
plus = "+ "
hash1 = "# "


for i in range(1, num * 2):
    if i <= num:
        left_spaces = spaces * (num - i)
        result = left_spaces + plus * (i - 1) + hash1
        print(result)
    else:
        left_spaces = spaces * (i - num)
        result = left_spaces + plus * (num * 2 - i - 1) + hash1
        print(result)
