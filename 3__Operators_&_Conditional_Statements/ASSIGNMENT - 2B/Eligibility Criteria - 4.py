M = int(input())
P = int(input())
C = int(input())

if (M + P + C >= 180) or (M + P >= 120 or C + P >= 110):
    print("True")
else:
    print("False")
