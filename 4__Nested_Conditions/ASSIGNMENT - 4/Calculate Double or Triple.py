N = int(input())

multiple = (N % 3) == 0
double = (N % 3) != 0

if multiple:
    print(N * 3)
elif double:
    print(N * 2)
