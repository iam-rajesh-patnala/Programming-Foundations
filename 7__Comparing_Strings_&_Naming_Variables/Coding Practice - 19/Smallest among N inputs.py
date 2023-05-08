num = int(input())

smallest = 100000000000000000000000000000000000000000

for i in range(num):
    num2 = int(input())
    if num2 <= smallest:
        smallest = num2
    print(smallest)

