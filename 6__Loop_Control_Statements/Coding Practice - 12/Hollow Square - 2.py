num = int(input())

spaces = "  "
hyphen = "- "
plus = "+ "
pipe = "| "


for i in range(1, num + 3):
    if i == 1 or i == num + 2:
        result = plus + hyphen * num + plus
        print(result)
    else:
        result = pipe + spaces * num + pipe
        print(result)
