num = int(input())

mul_two = []
mul_three = []

for i in range(1, num + 1):
    mul_two += [i * 2]
    mul_three += [i * 3]

union = set(mul_two) ^ set(mul_three)
op = set(mul_two) - set(mul_three)
op = list(op)
op.sort()

print(op)
print(list(union))
