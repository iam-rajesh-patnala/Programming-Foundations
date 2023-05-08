number_of_inputs = int(input())

first_input = int(input())
greatest_number = first_input

for i in range(number_of_inputs - 1):
    number = int(input())
    if number > greatest_number:
        greatest_number = number

print(greatest_number)
