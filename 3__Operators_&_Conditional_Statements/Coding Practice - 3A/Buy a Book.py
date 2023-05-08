S = input()
C = int(input())

if S == "large" and C <= 300:
    print("Buy a Book")
elif S == "small" and C < 300:
    print("Do Not Buy a Book")
