number = int(input())

for i in range(number):
    if (i == 0) or (i == (number - 1)):
        print("* " * number)
    else:
        number_of_spaces = "  " * (number - 2)
        print("* " + number_of_spaces + "* ")
