distance = int(input())

bonus = 50

first_40 = distance * 2 + bonus
second_20 = 40 * 2 + (distance - 40) * 4 + bonus
next_60 = 40 * 2 + 20 * 4 + (distance - 60) * 6 + bonus
above_120 = 40 * 2 + 20 * 4 + 60 * 6 + (distance - 120) * 8 + bonus

if distance <= 40:
    print(first_40)
elif 41 <= distance <= 60:
    print(second_20)
elif 61 <= distance <= 120:
    print(next_60)
elif distance > 120:
    print(above_120)
