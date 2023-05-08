N = int(input())

N = str(N)

length = len(N)

total = 0

for num in range(length):
    total += (int(N[num])) ** 4


if total == int(N):
    print("Armstrong Number")

else:
    print("Not an Armstrong Number")
