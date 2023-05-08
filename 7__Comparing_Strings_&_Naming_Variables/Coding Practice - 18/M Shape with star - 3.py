num = int(input())
zero = "0 "
dot = ". "

for i in range(1, num + 1):
    dots = dot * (num - i)
    val = dots + ((2 * i - 1) * zero) + dots
    print(val * 2)
