distance = int(input())

bonus = 30

first_20 = 20 * 2
next_40 = 40 * 4

if distance <= 20:
    score = distance * 2

elif distance <= 60:
    remaining_distance = distance - 20
    remaining_distance_score = remaining_distance * 4
    score = first_20 + remaining_distance_score
else:
    remaining_distance = distance - 60
    remaining_distance_score = remaining_distance * 6
    score = first_20 + next_40 + remaining_distance_score

score+= bonus

print(score)