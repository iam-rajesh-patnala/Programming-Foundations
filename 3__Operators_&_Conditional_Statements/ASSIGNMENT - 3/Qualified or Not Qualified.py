M = int(input())
P = int(input())

if (M > 35 and P > 35) or (M + P >= 100):
    print("Qualified")
else:
    print("Not Qualified")
