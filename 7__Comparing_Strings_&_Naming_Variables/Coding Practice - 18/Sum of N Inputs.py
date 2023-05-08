loop = int(input())

condition = float(input())

total = 0

for i in range(loop):
    input_val = float(input())
    total += input_val

rounded_total = round(total, 3)

if rounded_total == condition:
    print(True)
else:
    print(False)
