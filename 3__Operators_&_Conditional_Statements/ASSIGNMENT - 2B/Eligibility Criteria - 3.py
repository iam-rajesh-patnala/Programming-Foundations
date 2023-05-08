M = int(input())
P = int(input())
C = int(input())
if (M >= 35 and P >= 35 and C >= 35) and (M + C >= 90 or C + P >= 90 or P + M >= 90):
    print("True")
else:
    print("False")
