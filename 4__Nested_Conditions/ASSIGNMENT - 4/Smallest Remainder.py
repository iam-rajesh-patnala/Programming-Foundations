a = int(input())
b = int(input())

a_by_b = a % b
b_by_a = b % a

smallest = a_by_b > b_by_a

if smallest:
    print(b_by_a)
else:
    print(a_by_b)
