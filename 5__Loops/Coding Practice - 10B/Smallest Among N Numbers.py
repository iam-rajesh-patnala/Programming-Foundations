number_of_inputs = int(input())

first_input = int(input())
smallest_number = first_input

for i in range(number_of_inputs - 1):
    number = int(input())
    if number < smallest_number:
        smallest_number = number

print(smallest_number)
