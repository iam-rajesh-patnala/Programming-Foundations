M = int(input())
C = int(input())
P = int(input())

if M + P + C >= 180 and (M + P or M + C >= 100) and (M + P or M + C <= 100):
    print("True")
else:
    print("False")
