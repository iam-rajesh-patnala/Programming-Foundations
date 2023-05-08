num = int(input())

is_divisible = False

for i in range(2, 10):
    if num % i == 0:
        is_divisible = True

if is_divisible:
    print("Divisible Number")
else:
    print("Indivisible Number") 