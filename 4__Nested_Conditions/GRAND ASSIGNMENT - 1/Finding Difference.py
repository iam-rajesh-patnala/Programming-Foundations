N1 = int(input())
N2 = int(input())

grater = N1 > N2
less = N1 < N2


if grater:
    sub = N1 - N2
    print(sub)
elif less:
    sub = N2 - N1
    print(sub)
