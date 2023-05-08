A = int(input())
B = int(input())

result = ""
if (A > B):
    result = "Win"
elif (A == B):
    result = "Draw"
else:
    result = "Lose"

print (result)