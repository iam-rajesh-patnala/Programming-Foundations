D = int(input())

score = 0

if (D > 50):
    score += 50 * 3
    rem_distance = D - 50
    score += rem_distance * 5
elif (D <= 50):
    score += D * 3
else:
    print (score)

print(score)