input1 = input()
input1 = int(input1)

input2 = input()
input2 = int(input2)

is_grater_than = input1 > 5 or input2 > 5
is_positive = input1 > 0 and input2 > 0

result = is_grater_than and is_positive
print(result)
