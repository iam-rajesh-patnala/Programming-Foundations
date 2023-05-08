num = int(input())
first_input = int(input())
gretest_number = first_input

print(first_input)

for i in range(num-1):
    seq = int(input())
    if seq > gretest_number:
        gretest_number = seq
    print(gretest_number)
        