def show_numbers(number):
    for i in range(0, number + 1):
        if i == 0:
            print(str(i) + " EVEN")
        elif i % 2 == 0:
            print(str(i) + " EVEN")
        else:
            print(str(i) + " ODD")


number = int(input())
show_numbers(number)
